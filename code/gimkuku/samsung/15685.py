from copy import deepcopy

def rotatedir(d_lists):
    d_list = deepcopy(d_lists)
    r_list = []
    d_list.reverse()
    for i in d_list:
        if i == (0,1): r_list.append((-1,0))
        elif i == (-1,0):r_list.append((0,-1))
        elif i == (0,-1):r_list.append((1,0))
        elif i == (1, 0): r_list.append((0, 1))
    return r_list

def solution(n, curve):
    board = [[0 for i in range(101)]for j in range(101)]
    dirs = [(0,1),(-1,0),(0,-1),(1,0)]
    for x, y, d, g in curve:
        d_list = [dirs[d]]
        x_end, y_end = x, y
        board[x_end][y_end] = 1 
        for repeat in range(g + 1):
            # print("---------------------")
            # print("d_list",d_list)
            # print("---", x, y, d, repeat, "---")
            
            if repeat == 0: start = 0
            else: start = 2 ** (repeat - 1)
            for _d in d_list[start:]:
                x_end = x_end + _d[1]
                y_end = y_end + _d[0]
                board[x_end][y_end] = 1
                # print("(",x_end,",",y_end,")")
            r = rotatedir(d_list)
            d_list = d_list + r
    answer =0
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
                answer += 1
    print(answer)
    return
       
        


n = int(input())
curve = []
for i in range(n):
    curve.append(map(int, input().split()))
solution(n,curve)