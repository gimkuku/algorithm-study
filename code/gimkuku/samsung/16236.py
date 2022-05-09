from collections import deque

def solution(n, board):
    # 상어가 움직일 수 있는 방향
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    
    # 상어 처음 위치 찾기
    for idx,i in enumerate(board):
        for jdx,j in enumerate(i):
            if j == 9:
                sharkx, sharky = idx, jdx
                board[idx][jdx] = 0
                break

    # 상어 처음 크기
    shark = 2
    answer = 0
    cnt = 0
    eating = 0
    q = deque([])
    while True : 
        # 주변 물고기 탐색
        flag = True

        # 샤크 출발 할때 큐 초기화
        q=deque([[sharkx, sharky, answer]])
        visited = []
        caneat = []
        _mincnt = 999999999999

        while q:
            x, y, cnt = q.popleft()
            # print("현재 상어 위치", "현재위치", x,y, "움직인수", cnt)
            if (x, y) in visited:
                continue
            else: visited.append((x, y))
            
            # 최소 잡은 물고기 이동수보다 이동수 많아지면 멈추기
            if cnt > _mincnt:
                break
            
            # 물고기가 있으면 샤크 이동
            if board[x][y] != 0 and board[x][y] < shark:
                # print(visited)
                if cnt <= _mincnt:
                    _mincnt = cnt
                    caneat.append((x,y,cnt))
                flag = False

            # 먹을 수 있는 물고기도 없으면
            if (board[x][y] == 0 or board[x][y] == shark or board[x][y] == 9):
                for dx, dy in dirs:
                    if x + dx < 0 or x + dx > n -1 or y + dy < 0 or y + dy > n -1: continue
                    # 샤크 이동
                    if board[x + dx][y + dy] > shark: continue
                    if (x+dx, y+dy) in visited: continue
                    q.append([x + dx, y + dy, cnt+1])
        
        
        # 다 돌았는데 먹을 물고기 없으면 종료
        if flag:
            break
        else:
            # 물고기 중에 젤 왼쪽 위에 있는 애 먹기 
            caneat.sort(key=lambda x: (x[0],x[1]))
            # print(caneat)
            # print("물고기 먹기",caneat[0][0], caneat[0][1], shark)
            answer = caneat[0][2]
            eating += 1
            if eating == shark:
                shark += 1
                eating = 0
                # print("상어 연령 증가", shark)
            board[caneat[0][0]][caneat[0][1]] = 0
            sharkx = caneat[0][0]
            sharky = caneat[0][1]

    print(answer)
    

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
solution(n, board)
