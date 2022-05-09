from collections import deque
from itertools import permutations
from copy import deepcopy

answer = int(1e9)
adict = dict()
n_board = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def ctrl(d, r, c):
    global n_board
    
    while True:
        
        nr = r+dx[d]
        nc = c+dy[d]
        
        if 0>nr or nr>=4 or 0>nc or nc>=4:
            break
            
        if n_board[nr][nc] != 0:
            r, c = nr, nc
            break
        
        r, c = nr, nc
    
    return (r, c)


def bfs(sr, sc, dr, dc):
    global n_board
    visited = [[False] * 4 for _ in range(4)]
    
    # 만약 출발지와 목적지가 같은 경우
    if sr == dr and sc == dc:
        return 1 # Enter 1회만 counting
    
    q = deque()
    q.append((sr, sc, 0))
    visited[sr][sc] = True
    
    while q:
        cr, cc, cnt = q.popleft()
        
        for d in range(4):
            nr, nc = cr + dx[d], cc + dy[d]
            
            if 0<=nr<4 and 0<=nc<4:
                if visited[nr][nc] is False:
                    visited[nr][nc] = True
                    if nr == dr and nc == dc:
                        return cnt+2
                    else:
                        q.append((nr, nc, cnt+1))
                
                
            nr, nc = ctrl(d, cr, cc)
            
            if 0<=nr<4 and 0<=nc<4:
                if visited[nr][nc] is False:
                    visited[nr][nc] = True
                    if nr == dr and nc == dc:
                        return cnt+2
                    else:
                        q.append((nr, nc, cnt+1))

def remove(character_idx):
    global n_board, adict
    for r, c in adict[character_idx]:
        n_board[r][c] = 0
        
def recover(character_idx):
    global n_board, adict
    for r, c in adict[character_idx]:
        n_board[r][c] = character_idx

                
def back_tracking(r, c, order, idx, cnt):
    global answer, adict
    # 목적 back tracking을 하면서 1A, 1B 순서 왔다 갔다 하기
    if idx == len(order):
        answer = min(answer, cnt)
        return
    
    c1r, c1c = adict[order[idx]][0][0], adict[order[idx]][0][1]
    c2r, c2c = adict[order[idx]][1][0], adict[order[idx]][1][1]
    
    #### 시작점 -> 같은 character 카드 1 -> 같은 같은 character 카드 2 ####
    cost1 = bfs(r, c, c1r, c1c) # 시작점에서 첫번째 타겟과의 cost
    cost2 = bfs(c1r, c1c, c2r, c2c) # 첫번째 타겟에서 두번째 타겟과의 cost
    
    remove(order[idx]) # character_idx 카드 없애기
    back_tracking(c2r, c2c, order, idx+1, cnt+cost1+cost2) # 같은 같은 character 카드 2 -> 다음 카드 묶음  dfs
    recover(order[idx]) # backtraking 후 다시 character_idx 살리기
    
    
    ### 시작점 -> 같은 character 카드 2 -> 같은 같은 character 카드 1 ###
    cost1 = bfs(r, c, c2r, c2c) # 시작점에서 두번째 타겟과의 cost
    cost2 = bfs(c2r, c2c, c1r, c1c) # 두번째 타겟에서 첫번째 타겟과의 cost
    
    remove(order[idx]) # character_idx 카드 없애기
    back_tracking(c1r, c1c, order, idx+1, cnt+cost1+cost2) # 같은 같은 character 카드 1 -> 다음 카드 묶음  dfs
    recover(order[idx]) # backtraking 후 다시 character_idx 살리기
    
    
            

def solution(board, r, c):
    global answer, adict, n_board
    
    # borad를 global로 사용하기 위해 deepcopy
    n_board = deepcopy(board)
    
    # board를 완전탐색하여 adict에 캐릭터 별로 분류
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in adict.keys():
                    adict[board[i][j]] = [(i, j)]
                else:
                    adict[board[i][j]].append((i, j))
                    
    character = list(adict.keys())
    print(character)
    orders = list(permutations(character, len(character)))
    
    
    for order in orders:
        # order = (1, 3, 2)
        back_tracking(r, c, order, 0, 0)
        
    
    return answer