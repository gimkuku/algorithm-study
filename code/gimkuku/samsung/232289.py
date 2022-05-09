def solution(r, c, k, b, wall):
    # 1: 오른쪽 온풍기 2: 왼쪽 온풍기 3: 위 온풍기 4: 아래 온풍기
    heat_dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    wall_dirs = [()]
    check = []
    heat = []
    board = [[0 for i in range(c)] for j in range(r)]
    print(wall)

    # 온풍기 위치 적어놓기 
    for x in range(r):
        for y in range(c):
            if b[x][y] == 5:
                check.append((x, y))
            elif b[x][y] != 0:
                heat.append([x,y,b[x][y]-1]) 

    # 온풍기 별 바람불기
    for x, y, d in heat:
        dx, dy = heat_dirs[d]
        prev = [(x,y)]
        prevxmax = x
        prevxmin = x
        prevymax = y
        prevymin = y
        for i in range(5):
            x = x + dx
            y = y + dy

            if i == 0:
                prevx, prevy = prev.pop(0)
                prevx += dx
                prevy += dy
                if prevx < 0 or prevy < 0 or prevx > r-1 or prevy > c-1: continue
                if str(prevx) + "_" + str(prevy) in wall: continue
                board[prevx][prevy] += 5 - i
                prev=[(prevx,prevy)]
                continue  # 양 옆 안가고 멈추기
            
            
            n_prev = []
            # 앞으로 이동 먼저 
            for prevx, prevy in prev:
                prevx += dx
                prevy += dy
                if prevx < 0 or prevy < 0 or prevx > r -1 or prevy > c-1: continue
                if str(prevx)+"_"+str(prevy) in wall: continue
                board[prevx][prevy] += 5 - i
                n_prev.append((prevx,prevy))
            
            # 양옆로 움직일때
            for x, y in [prev.pop(0), prev.pop(-1)]:
                x += dx
                y += dy
                
                if dx == 0:
                    # 대각선 위
                    if x + i < r:
                        if str(x+1) + "_" + str(y) in wall: continue
                        if str(x + 1) + "_" + str(y + dy) in wall: continue
                        if prevxmax + 1 > r-1 : continue
                        board[prevxmax + 1][y] += 5 - i
                        n_prev.append((prevxmax + 1,y))
                        prevxmax += 1

                    # 대각선 아래
                    if x - i > 0:
                        if str(x-1) + "_" + str(y) in wall: continue
                        if str(x - 1) + "_" + str(y + dy) in wall: continue
                        if prevxmin - 1 < 0: continue
                        board[prevxmin - 1][y] += 5 - i
                        n_prev.append((prevxmin - 1,y))
                        prevxmin -= 1

                # 위아래으로 움직일때
                else:
                    # 오른쪽 
                    if y + i < c:
                        if str(x) + "_" + str(y+1) in wall: continue
                        if str(x + dx) + "_" + str(y + 1) in wall: continue
                        if prevymax + 1 > c: continue
                        board[x][prevymax + 1] += 5 - i
                        n_prev.append((x,prevymax + 1))
                        prevymax += 1
                    # 왼쪽
                    if y - i > 0:
                        if str(x) + "_" + str(y-1) in wall: continue
                        if str(x + dx) + "_" + str(y - 1) in wall: continue
                        if prevymin - 1 < 0: continue
                        board[x][prevymin - 1] += 5 - i
                        n_prev.append((x,prevymin - 1))
                        prevymin -= 1

                # prev 업데이트
                prev = n_prev
                print("i",i,"n_prev",n_prev,"prev",prev)
    for i in range(r):
        print(board[i])
                    
                



r, c, k  = map(int, input().split())
b = []
for i in range(r):
    b.append(list(map(int, input().split())))
w = int(input())

wall = {}
for i in range(w):
    x, y, d = map(int, input().split())
    key = str(x-1) + "_" + str(y-1)
    if key in wall:
        wall[key] += [d]
    else:
        wall[key] = [d]

solution(r, c, k, b, wall)


# 바람이 오른쪽으로 불었을 때 = (dy + 1)하는 상황

# i) (x,y) -> (x-1,y+1) : 오른쪽 위로 이동
# (x, y)와 (x-1, y) 사이에 벽이 없어야 하고, (위아래)
# (x-1, y)와 (x-1, y+1) 사이에도 벽이 없어야 한다. (위에서 오른쪽 양옆)
# 즉, 바람이 위로갔다가 오른쪽으로 감
# dx -1 -> dy +1 

# ii)(x, y)  -> (x, y+1) : 오른쪽 이동
# (x, y), (x, y+1) (오른쪽 양옆)
# dy + 1

# iii) (x, y) -> (x+1, y+1) : 오른쪽 아래로 이동
# (x, y)와 (x+1, y) : 아래위
# (x+1, y)와 (x+1, y+1) : 아래에서 오른쪽 양옆
# 즉 아래로 이동하고 오른쪽으로 이동
# dx +1 -> dy +1