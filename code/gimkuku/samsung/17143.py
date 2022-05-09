def solution(r, c, m, shark, board):
    answer = 0
    
    dirs = [(-1,0),(1,0),(0,1),(0,-1)]
    for f in range(c):
        if m == 0:
            print(answer)
            return

        # 낚시 하기
        for i in range(r):
            if board[i][f] != -1:
                answer += shark[board[i][f]][4]
                shark.remove(shark[board[i][f]])
                board[i][f] = -1
                m -= 1
                break

        # 상어 옮기기
        idx = 0
        for x, y, s, d, z in shark:
            dx, dy = dirs[d]
            for _ in range(s):
                # 범위 넘어가면 방향 바꾸기 
                if shark[idx][0] + dx < 0 or shark[idx][0] + dx > r - 1 or shark[idx][1] + dy < 0 or shark[idx][1] + dy > c - 1:
                    if (shark[idx][3] % 2): shark[idx][3] -= 1
                    else: shark[idx][3] += 1
                    dx, dy = dirs[shark[idx][3]]
                shark[idx][0] += dx
                shark[idx][1] += dy
            idx += 1
            
        # 중복 상어 찾기
        board = [[-1 for i in range(c)] for j in range(r)]
        shark.sort(key=lambda x: x[4], reverse=True)
        idx = 0
        for x, y, s, d, z in shark[:]:
            if board[x][y] == -1:
                board[x][y] = idx
                idx += 1
            else:
                shark.remove([x, y, s, d, z])
                m -= 1
        # for i in board:
        #     print(i)
        # print("\n")
    print(answer)
    return
                    


r, c, m = map(int, input().split())
shark = []
board = [[-1 for i in range(c)] for j in range(r)]

for i in range(m):
    _r, _c, _s, _d, _z = map(int, input().split())
    if _d == 1 or _d== 2:
        if _s > (r - 1) * 2: _s = _s % ((r - 1) * 2)
    elif _d == 3 or _d == 4:
        if _s > (c - 1) * 2: _s = _s % ((c - 1) * 2)
    shark.append([_r - 1, _c - 1, _s, _d - 1, _z])
    # 상어 번호
    board[_r -1][_c-1] = i


# print(shark)
solution(r, c, m, shark,board)
