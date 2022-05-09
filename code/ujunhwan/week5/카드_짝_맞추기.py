from collections import deque

def solution(board, r, c):
    total = 0
    pos = [[] for _ in range(10)]
    visited = [[False for col in range(4)] for row in range(4)]
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                total += 1
                pos[board[i][j]].append([i, j])
    
    def find(y, x):
        val = board[y][x]
        for ny, nx in pos[val]:
            if y == ny and x == nx:
                continue
            return ny, nx
    
    def is_valid(y, x):
        if 0 <= y < 4 and 0 <= x < 4:
            return True
       	return False
    
    def calc_dist(cur, goal):
        y, x = cur
        gy, gx = goal
        
        INF = 987654321
        visited = [[False for col in range(4)] for row in range(4)]
        dist = [[INF for col in range(4)] for row in range(4)]
        
        q = deque()
        q.append([y, x])
        dist[y][x] = 0
        
        for i in range(y+1, 4):
            if board[i][x] > 0 or i == 3:
                q.append([i, x])
                dist[i][x] = 1
                break
        
        for i in range(y-1, -1, -1):
            if board[i][x] > 0 or i == 0:
                q.append([i, x])
                dist[i][x] = 1
                break
            
        for j in range(x+1, 4):
            if board[y][j] > 0 or j == 3:
                q.append([y, j])
                dist[y][j] = 1
                break
            
        for j in range(x-1, -1, -1):
            if board[y][j] > 0 or j == 0:
                q.append([y, j])
                dist[y][j] = 1
                break
        
        while q:
            cy, cx = q.popleft()
            val = dist[cy][cx]
            
            for i in range(cy+1, 4):
                if board[i][cx] > 0 and dist[i][cx] != INF:
                    break
                if (board[i][cx] > 0 or i == 3) and dist[i][cx] == INF:
                    q.append([i, cx])
                    dist[i][cx] = val + 1
                    break
        
            for i in range(cy-1, -1, -1):
                if board[i][cx] > 0 and dist[i][cx] != INF:
                    break
                if (board[i][cx] > 0 or i == 0) and dist[i][cx] == INF:
                    q.append([i, cx])
                    dist[i][cx] = val + 1
                    break

            for j in range(cx+1, 4):
                if board[cy][j] > 0 and dist[cy][j] != INF:
                    break
                if (board[cy][j] > 0 or j == 3) and dist[cy][j] == INF:
                    q.append([cy, j])
                    dist[cy][j] = val + 1
                    break

            for j in range(cx-1, -1, -1):
                if board[cy][j] > 0 and dist[cy][j] != INF:
                    break
                if (board[cy][j] > 0 or j == 0) and dist[cy][j] == INF:
                    q.append([cy, j])
                    dist[cy][j] = val + 1
                    break
            
            for k in range(4):
                ny, nx = cy + dy[k], cx + dx[k]
               	if is_valid(ny, nx) and val+1 < dist[ny][nx]:
                    q.append([ny, nx])
                    dist[ny][nx] = val + 1
        
        return dist[gy][gx]
    
    def dfs(y, x, left):
        if left <= 0:
            return 0
        
        ret = 9876543210
        
        if board[y][x] == 0:
            for i in range(4):
                for j in range(4):
                    if board[i][j] == 0: continue
                    dist = calc_dist([y, x], [i, j])
                    ret = min(ret, dfs(i, j, left) + dist)
        
        # choose
        if board[y][x] > 0:
            ny, nx = find(y, x)
            val = board[y][x]
            dist = calc_dist([y, x], [ny, nx])
            board[y][x] = 0
            board[ny][nx] = 0
            ret = min(ret, dfs(ny, nx, left-1) + dist)
            board[y][x] = val
            board[ny][nx] = val
        
        return ret
    
    answer = dfs(r, c, total//2) + total
    return answer