from itertools import combinations
from copy import deepcopy
direct = ((0,1),(0,-1),(1,0),(-1,0))
def dfs(i, j, board,visited):
    visited[i][j] = 0
    if board[i][j] == 1:
        return
    else:
        board[i][j] = 2
        for d in range(4):
            if i + direct[d][0] < 0 or i + direct[d][0] > n - 1 or j + direct[d][1] < 0 or j + direct[d][1] > m - 1:
                continue
            else:
                if visited[i + direct[d][0]][j + direct[d][1]]:
                    dfs(i + direct[d][0], j + direct[d][1], board,visited)
        return
                
def count(board):
    cnt = 0
    visited = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                dfs(i,j,board,visited)
    
    for i in board:
        cnt += i.count(0)
    return cnt

def solution(n, m, b):
    _max = 0
    items = []
    for i in range(n):
        for j in range(m):
            items.append((i, j))

    # 벽 좌표 계산
    walls = list(combinations(items, 3))

    for i in walls:
        # print(i)
        flag = True
        board = deepcopy(b)
        for j in range(3):
            if board[i[j][0]][i[j][1]] != 0:
                flag = False
                break
            board[i[j][0]][i[j][1]] = 1
        if flag:
            temp = count(board)
            if temp > _max:
                _max = temp
    print(_max)


n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

solution(n, m,board)
