# from copy import deepcopy
import sys
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, value, steps):
    global _max
    if x < 0 or y < 0 or x > n-1 or y > m-1:
        return
    # 이미 방문했던 점
    if board[x][y] == 0:
        if steps == 3:
            for i in range(4):
                if x + d[i][0] < 0 or y + d[i][1] < 0 or x + d[i][0] > n-1 or y + d[i][1] > m-1:
                    continue
                if board[x + d[i][0]][y + d[i][1]] != 0:
                    dfs(x + d[i][0], y + d[i][1], value, steps)
            return
        else:
            return 
    # 처음 방문하는 점
    else:
        steps += 1
        now = board[x][y]
        value += now
        board[x][y] = 0
        if steps == 4:
            if _max < value:
                _max = value
            board[x][y] = now
            return value
        elif steps < 4:
            if steps != 3:
                for i in range(4):
                    if x + d[i][0] < 0 or y + d[i][1] < 0 or x + d[i][0] > n-1 or y + d[i][1] > m-1:
                        continue
                    if board[x + d[i][0]][y + d[i][1]] != 0:
                        dfs(x + d[i][0], y + d[i][1], value, steps)
            else:
                for i in range(4):
                    if x + d[i][0] < 0 or y + d[i][1] < 0 or x + d[i][0] > n-1 or y + d[i][1] > m-1:
                        continue
                    if board[x + d[i][0]][y + d[i][1]] != 0:
                        dfs(x + d[i][0], y + d[i][1], value, steps)
                    else:
                        dfs(x + d[i][0], y + d[i][1], value, steps)
            board[x][y] = now
            return
    return

def solution(n, m, _board):
    global _max, visited,board
    _max = 0
    visited = {}
    board =  _board
    for i in range(n):
        for j in range(m):
            dfs(i, j, 0, 0)
    print(_max)
    return _max


n, m = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
solution(n,m,board)