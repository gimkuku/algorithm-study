from collections import deque

def solution(board):
    N = len(board[0])
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    def is_valid(y, x):
        return 0 <= y < N and 0 <= x < N
    
    def rotate(pos, mode, d):
        # rotate -> change robot pos, mode
        y, x = pos // N, pos % N
        
        # horizontal
        if mode == 0:
            if d == 0:
                if not is_valid(y-1, x) or board[y-1][x] == 1:
                    return False, [y, x, 0]
                if not is_valid(y-1, x+1) or board[y-1][x+1] == 1:
                    return False, [y, x, 0]
                return True, [y-1, x+1, 1]
            elif d == 1:
                if not is_valid(y+1, x) or board[y+1][x] == 1:
                    return False, [y, x, 0]
                if not is_valid(y+1, x+1) or board[y+1][x+1] == 1:
                    return False, [y, x, 0]
                return True, [y, x+1, 1]
            elif d == 2:
                if not is_valid(y+1, x+1) or board[y+1][x+1] == 1:
                    return False, [y, x, 0]
                if not is_valid(y+1, x) or board[y+1][x] == 1:
                    return False, [y, x, 0]
                return True, [y, x, 1]
            elif d == 3:
                if not is_valid(y-1, x+1) or board[y-1][x+1] == 1:
                    return False, [y, x, 0]
                if not is_valid(y-1, x) or board[y-1][x] == 1:
                    return False, [y, x, 0]
                return True, [y-1, x, 1]
                
        else:
            if d == 0:
                if (not is_valid(y, x-1) or board[y][x-1] == 1) or \
                (not is_valid(y+1, x-1) or board[y+1][x-1] == 1):
                    return False, [y, x, 1]
                return True, [y+1, x-1, 0]
            elif d == 1:
                if (not is_valid(y+1, x-1) or board[y+1][x-1] == 1) or \
                (not is_valid(y, x-1) or board[y][x-1] == 1):
                    return False, [y, x, 1]
                return True, [y, x-1, 0]
            elif d == 2:
                if (not is_valid(y, x+1) or board[y][x+1] == 1) or \
                (not is_valid(y+1, x+1) or board[y+1][x+1] == 1):
                    return False, [y, x, 1]
                return True, [y+1, x, 0]
            elif d == 3:
                if (not is_valid(y+1, x+1) or board[y+1][x+1] == 1) or \
                (not is_valid(y, x+1) or board[y][x+1] == 1):
                    return False, [y, x, 1]
                return True, [y, x, 0]
    
    def can_go(pos, npos, mode):
        y, x = pos//N, pos%N
        ny, nx = npos//N, npos%N
        y2, x2 = y, x
        if mode == 0:
            y2, x2 = y, x+1
            ny2, nx2 = ny, nx+1
        else:
            y2, x2 = y+1, x
            ny2, nx2 = ny+1, nx
        
        if not is_valid(ny2, nx2) or board[ny2][nx2] == 1:
            return False
        if not is_valid(ny, nx) or board[ny][nx] == 1:
            return False
        return True
    
    q = deque()
    q.append([0, 0])
    dist = [[float('inf') for _ in range(2)] for __ in range(10001)]
    dist[0][0] = 0
    
    while q:
        pos, mode = q.popleft()
        y, x = pos // N, pos % N
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            npos = ny*N+nx
            if is_valid(ny, nx):
                if can_go(pos, npos, mode) and dist[npos][mode] > dist[pos][mode] + 1:
                    dist[npos][mode] = dist[pos][mode] + 1
                    q.append([npos, mode])
        
        # rotate
        # pos = y*N+x
        for k in range(4):
            is_success, [ny, nx, nmode] = rotate(pos, mode, k)
            npos = ny*N+nx
            if is_success and dist[npos][mode^1] > dist[pos][mode] + 1:
                dist[npos][mode^1] = dist[pos][mode] + 1
                q.append([npos, mode^1])
                
                '''
    print(dist[:25])
    for i in range(5):
        for j in range(5):
            print(f"{i} {j} dist : {dist[i*N+j]}")
            '''
    
    y, x = N-1, N-1
    answer = min(dist[y*N+(x-1)][0], dist[(y-1)*N+x][1])
    return answer