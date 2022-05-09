from collections import deque
from copy import deepcopy
def back(now):
    if now == 0:
        return 2
    elif now == 1:
        return 3
    elif now == 2:
        return 0
    elif now == 3:
        return 1
def left(now):
    if now == 0:
        return 3
    elif now == 1:
        return 0
    elif now == 2:
        return 1
    elif now == 3:
        return 2

def solution(n, m, r, c, d, board):
    wall = deepcopy(board)
    d_list = [[-1,0],[0,1],[1,0],[0,-1]]
    q = deque([(r, c, d)])
    cnt = 0
    while q:
        # print(q)
        x, y, direct = q.popleft()
        if board[x][y] == 0:
            cnt+=1
        board[x][y] = 1
        nextd = left(direct)
        # 왼쪽으로 갈 수 있으면 이동
        if x + d_list[nextd][0] > -1 or y + d_list[nextd][1] > -1 or x + d_list[nextd][0] < n or y + d_list[nextd][1] < m:    
            if board[x + d_list[nextd][0]][y + d_list[nextd][1]] == 0:
                q.append((x + d_list[nextd][0], y + d_list[nextd][1], nextd))
                continue

        # 아니면 회전만    
        flag = True
        for i in range(4):
            nextd = left(nextd)
            if x + d_list[nextd][0] > -1 or y + d_list[nextd][1] > -1 or x + d_list[nextd][0] < n or y + d_list[nextd][1] < m:
                if board[x + d_list[nextd][0]][y + d_list[nextd][1]] == 0:
                    flag = False
                    q.append((x + d_list[nextd][0], y + d_list[nextd][1], nextd))
                    break
        
        # 아니면 후진 할 수 있음 후진하기
        if flag:
            # print(direct)
            _back = back(direct)
            if x + d_list[_back][0] > -1 or y + d_list[_back][1] > -1 or x + d_list[_back][0] < n or y + d_list[_back][1] < m:
                if wall[x + d_list[_back][0]][y + d_list[_back][1]] == 0:
                    q.append((x + d_list[_back][0], y + d_list[_back][1], direct))
            else:
                break
    print(cnt)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
solution(n,m,r,c,d,board)