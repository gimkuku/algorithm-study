from copy import deepcopy
from itertools import product

def cnt(d, b):
    global n,m
    dir1 = [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]]
    dir2 = [[(0, 1),(0, -1)], [(1, 0),(-1, 0)], [(0, 1),(0, -1)], [(1, 0),(-1, 0)]]
    dir3 = [[(0, 1),(1, 0)], [(0, 1),(-1, 0)], [(0, -1),(1, 0)], [(0, -1),(-1, 0)]]
    dir4 = [[(0, -1),(1, 0),(-1, 0)], [(0, 1),(-1, 0),(1, 0)], [(1, 0),(0, -1),(0, 1)], [(-1, 0),(0, -1),(0, 1)]]
    dir5 = [[(0, 1),(1, 0),(-1, 0),(0,-1)]]
    directs = [dir1, dir2, dir3, dir4, dir5]

    d_cnt = 0
    for idx, i in enumerate(b):
        for jdx, j in enumerate(i):
            if j == "#" : continue
            if j == 0 or j == 6: continue
            if j == 5:
                direct = directs[4][0]
            else:
                direct = directs[j - 1][d[d_cnt]]
                d_cnt += 1
            for di in direct:
                x,y = idx,jdx
                while True:
                    x = x + di[0]
                    y = y + di[1]
                    if (x < 0 or y < 0 or x > n - 1 or y > m - 1):
                        break
                    if b[x][y] == 6: break
                    if b[x][y] != 0: continue
                    else:
                        b[x][y] = "#"
                    
    _cnt = 0
    for i in b:
        _cnt += i.count(0)
    return _cnt
                
def solution(_n, _m, board):
    global n, m
    n,m = _n,_m
    direct = []
    _min = float('inf')
    _cnt = 0
    iters = []
    nums = 0
    # 완탐용 배열 만들기
    for i in board:
        for j in i:
            if j == 0 or j == 6 or j == 5:
                continue
            else:
                nums += 1

    iters = list(map(list,product([0,1,2,3],repeat = nums)))
    for i in iters:
        b = deepcopy(board)
        temp = cnt(i,b)
        if (_min > temp):
            _min = temp
            # for i in b:
            #     print(i)
            # print("\n")
    print(_min)


n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    
solution(n, m, board)
