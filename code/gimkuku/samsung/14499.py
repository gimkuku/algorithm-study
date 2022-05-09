def solution(n, m, x, y, k, board, direct):
    dice = [0, 0, 0, 0, 0, 0]
    top = 1
    bot = 7-top
    front = 2
    back = 7-front
    left = 3
    right = 7 - left
    
    di = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    for i in direct:
        if (x + di[i - 1][0] < 0 )or (y + di[i - 1][1] < 0) or (x + di[i - 1][0] > n - 1 )or (y + di[i - 1][1] > m - 1):
            continue
        # print(dice)
        if i == 1:
            right = top
            top = left
            left = 7 - right
            bot = 7- top
        elif i == 2:
            left = top
            top = right
            right = 7 - left
            bot = 7- top
        elif i == 3:
            top = front
            front = bot
            bot = 7 - top
            back = 7 - front
        elif i == 4:
            top = back
            back = bot
            bot = 7 - top
            front = 7 - back

        
        x = x + di[i - 1][0]
        y = y + di[i - 1][1]
        # print("front",front,"left",left,"top",top)
        # print("board", board)
        # print("bottom", dice[bot - 1])
        # print("board x y",board[x][y], x,y)
        
        if board[x][y] == 0:
            board[x][y] = dice[bot -1]
        else:
            dice[bot - 1] = board[x][y]
            board[x][y] = 0
        print(dice[top-1])



n, m, x, y, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
direct = []
for j in input().split():
    direct.append(int(j))

solution(n,m,x,y,k,board,direct)
