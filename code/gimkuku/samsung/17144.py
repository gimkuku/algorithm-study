def solution(r, c, t, board):
    # 공기 청정기 위치 찾기
    airx = 0
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(r):
        if board[i][0] == -1:
            airx = i
            break
    
    # t초 동안
    for time in range(t):
        # print("------------",time,"--------------")
        # for i in board:
        #     print(i)
        # print(board)
        # 미세먼지 확산
        misae = []
        for x, i in enumerate(board):
            for y, j in enumerate(i):
                if j != 0 and j != -1:
                    misae.append((x * c + y, j))

        for xy, data in misae:
            x, y = xy // c, xy % c
            possible = 0
            for dx, dy in dirs:
                if (x + dx < 0 or y + dy < 0 or x + dx > r - 1 or y + dy > c - 1): continue
                if (board[x + dx][y + dy] == -1): continue
                possible += 1
                board[x + dx][y+dy] += data // 5
            board[x][y] -= ((data // 5) * possible)
        
        # 공기 청정 윗부분
        for i in range(airx-2, -1, -1):
            board[i + 1][0] = board[i][0]
        for i in range(0, c-1 ):
            board[0][i] = board[0][i+1]
        for i in range(1, airx + 1):
            board[i - 1][c-1] = board[i][c-1]
        for i in range(c-2, 0, -1):
            board[airx][i+1] = board[airx][i]
        board[airx][1] = 0
        # 공기 청정 아래부분
        for i in range(airx+3,r):
            board[i - 1][0] = board[i][0]
        for i in range(0, c-1):
            board[r-1][i] = board[r-1][i + 1]
        for i in range(r-2, airx, -1):
            board[i + 1][c-1] = board[i][c-1]
        for i in range(c-2, 0, -1):
            board[airx +1][i+1] = board[airx +1][i]
        board[airx +1][1] = 0
        board[airx][0], board[airx + 1][0] = -1, -1
    
    # print("------------",time,"--------------")
    # for i in board:
    #     print(i)

    cnt = 2                
    for i in board:
        for j in i:
            cnt += j
    print(cnt)
            


r, c, t = map(int, input().split())
board = []
for i in range(r):
    board.append(list(map(int, input().split())))
    
solution(r,c,t,board)