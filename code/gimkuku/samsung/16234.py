from collections import deque

def solution(n, l, r, board):
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    m = len(board[0])
    visited = [[0 for i in range(m)] for j in range(n)]
    q = deque([])

    cnt = 1
    is_union = False
    answer = 0

    while is_union or cnt != 0:
        # 다 방문했으면 전체 초기화
        if cnt == 0:
            answer += 1
            is_union = False
            visited = [[0 for i in range(m)] for j in range(n)]
            cnt = n*m

        # print(visited)
        flag = False
        # 미방문 지점 찾기
        for idx,i in enumerate(visited):
            for jdx,j in enumerate(i):
                if j == 0:
                    for dx, dy in dirs:
                        if idx + dx < 0 or jdx + dy < 0 or idx + dx > n - 1 or jdx + dy > m - 1:
                            continue
                        diff = max(board[idx][jdx], board[idx + dx][jdx + dy]) - min(board[idx][jdx], board[idx + dx][jdx + dy])
                        if diff >= l and diff <= r:
                            q.append([idx, jdx])
                            flag = True
                            break
                    
                if flag: break
                else: visited[idx][jdx] = 1
            if flag: break
            

        
        # 새로운 연합 시작
        _sum = 0
        _n = 0
        path = []
        while q:
            x, y = q.popleft()
            if visited[x][y] == 1: continue
            else: visited[x][y] = 1

            _sum += board[x][y]
            _n += 1
            path.append((x) * m + y)
            for dx, dy in dirs:
                if x + dx < 0 or y + dy < 0 or x + dx > n - 1 or y + dy > m - 1:
                    continue
                if visited[x + dx][y + dy]: continue
                # 인구차가 n명 이상이면 연합!!! 
                diff = max(board[x][y], board[x + dx][y + dy]) - min(board[x][y], board[x + dx][y + dy])
                if diff >= l and diff <= r:
                    # 연합할게 있다! 
                    is_union = True
                    q.append([x + dx, y + dy])

        # 더이상 이동할 곳 없으면 계산
        if is_union:
            for i in path:
                x, y = i // m, i % m
                board[x][y] = _sum // _n
        
        # visited 안한곳 찾기
        cnt = 0
        for v in visited:
            cnt += v.count(0)
    print(answer)

n, l, r = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
solution(n,l,r,board)