from itertools import combinations
from collections import deque

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def calc(originx, originy, board, chics):
    _min = float('inf')
    for i in chics:
        idx, jdx = i // n, i % n
        temp = max(idx, originx) - min(idx, originx) + max(jdx, originy) - min(jdx, originy)
        if _min > temp:
            _min = temp
    return _min
        

def solution(n, m, board):
    chickens = []
    for idx,i in enumerate(board):
        for jdx,j in enumerate(i):
            if j == 2:
                chickens.append(idx * n + jdx)
                # 일단 치킨집 없애기
                board[idx][jdx] = 0
    # print(board)
    ch_list = list(map(list,combinations(chickens, m)))
    # print(ch_list)
    answer = 9999999999
    for i in ch_list:
        ch_road = 0
        for loc in i:
            x, y = loc // n, loc % n
            board[x][y] = 2
        for xdx,_x in enumerate(board):
            for ydx, _y in enumerate(_x):
                if _y == 1:
                    ch_road += calc(xdx,ydx,board,i)
        if answer > ch_road:
            answer = ch_road
        for loc in i:
            x, y = loc // n, loc % n
            board[x][y] = 0
    print(answer)
    return

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
solution(n,m,board)