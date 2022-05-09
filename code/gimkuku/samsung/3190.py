from collections import deque

def changedir(now, dir):
    if now == (0, 1):
        if dir == "L": return (-1,0)
        else:return (1,0)
    if now == (0, -1):
        if dir == "L":return (1,0)
        else:return(-1,0)
    if now == (1, 0):
        if dir == "L":return (0,1)
        else:return(0,-1)
    if now == (-1, 0):
        if dir == "L": return(0,-1)
        else:return(0,1)
def solution(n, apple, snake):
    board = []
    for i in range(n):
        element = []
        for j in range(n):
            if i == 0 and j == 0:
                element.append("S")
            elif [str(i+1), str(j+1)] in apple:
                element.append("A")
            else:
                element.append("0")
        board.append(element)
    # print(board)

    time = 0
    dx,dy = 0, 1
    hx, hy = 0, 0
    q = deque([(0,0)])
    while True:
        
        # print("time",time)
        # print(board)
        # print("dir", dx, dy)
        # print("snake",snake)
        for i in snake:
            if str(time) == i[0]:
                # print("changedir",str(time),i[0])
                dx, dy = changedir((dx, dy), i[1])
                break
        if hx + dx < 0 or hy + dy < 0 or hx + dx >= n or hy + dy >= n:
            print(time + 1)
            return time
        if board[hx + dx][hy + dy] == "S":
            print(time + 1)
            return time
        elif board[hx + dx][hy + dy] == "A":
            board[hx + dx][hy + dy] = 'S'
            hx += dx
            hy += dy
            q.append((hx,hy))
        else:
            board[hx + dx][hy + dy] = 'S'
            hx += dx
            hy += dy
            q.append((hx,hy))
            tx, ty = q.popleft()
            board[tx][ty] = '0'
        
        time += 1
        

n = int(input())
k = int(input())
apple = []
for i in range(k):
    a = input().split()
    apple.append(a)
l = int(input())
snake = []
for j in range(l):
    s = input().split()
    snake.append(s)
solution(n, apple,snake)