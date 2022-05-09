from collections import deque

N = None

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = None

def check_boundary(a, b, c, d):
    # 이동한 위치가 지도 안에 있는지 확인
    if 0<=a<N and 0<=b<N and 0<=c<N and 0<=d<N:
        return True
    else:
        return False

def change_rot(shape):
    # 만약 로테이션이면 모양을 바꾸어준다
    # v (세로인 경우) -> h (가로로)
    if shape == 'v':
        return 'h'
    # h (가로인 경우) -> v (세로로)
    else:
        return 'v'

def check_visited(a, b, c, d, shape):
    global visited
    
    if shape == 'h':
        s = 0
    else:
        s = 1
        
    if visited[s][a][b] == True and visited[s][c][d] == True:
        return False
    else:
        # 방문할 것이므로 visited 처리까지 한다
        visited[s][a][b] = True 
        visited[s][c][d] = True
        return True
        
        

def rotation_v(rot_num, board, a, b, c, d, shape):
    # 회전 가능 
    
    # 회전시, 방향이 무조건 바뀌기 때문에 
    ns = change_rot(shape)
    
    # c,d가 더 위에 있는 경우 a,b 와 c,d 자리 바꾸기
    if a > c:
        a, c = c, a
        b, d = d, b
    
    # (a,b)(c,d) -> (a+1,b-1)(c,d) 조건 (a,b-1)이 1이 아니어야
    if rot_num == 0:
        na, nb = a+1, b-1
        if check_boundary(na, nb, c, d):
            if board[a][b-1] != 1 and check_visited(na, nb, c, d, ns):
                return (True, na, nb, c, d, ns)

    # (a,b)(c,d) -> (a+1,b+1)(c,d) 조건 (a,b+1)가 1이 아니어야
    if rot_num == 1:
        na, nb = a+1, b+1
        if check_boundary(na, nb, c, d) :
            if board[a][b+1] != 1 and check_visited(na, nb, c, d, ns):
                return (True, na, nb, c, d, ns)
            
    # (a,b)(c,d) -> (a,b)(c-1,d-1) 조건 (c,d-1)가 1이 아니어야
    if rot_num == 2:
        nc, nd = c-1, d-1
        if check_boundary(a, b, nc, nd) :
            if board[c][d-1] != 1 and check_visited(a, b, nc, nd, ns):
                return (True, a, b, nc, nd, ns)
            
    # (a,b)(c,d) -> (a,b)(c-1,d+1) 조건 (c,d+1)가 1이 아니어야
    if rot_num == 3:
        nc, nd = c-1, d+1
        if check_boundary(a, b, nc, nd) :
            if board[c][d+1] != 1 and check_visited(a, b, nc, nd, ns):
                return (True, a, b, nc, nd, ns)
            
    return (False, a, b, c, d, shape)
    

def rotation_h(rot_num, board, a, b, c, d, shape):
    # 회전 가능 
    # (a,b)(c,d) -> (a+1,b+1)(c,d) 조건 (a+1,b)이 1이 아니어야
    
    ns = change_rot(shape)
    
    # a, b가 오른쪽에 있는 경우 c,d와 swap 해준다
    if b>d:
        a, c = c, a
        b, d = d, b
    
    # (a,b)(c,d) -> (a+1,b+1)(c,d) 조건 (a+1,b)가 1이 아니어야
    if rot_num == 0:
        na, nb = a+1, b+1
        if check_boundary(na, nb, c, d):
            if board[a+1][b] != 1 and check_visited(na, nb, c, d, ns):
                return (True, na, nb, c, d, ns)

    # (a,b)(c,d) -> (a-1,b+1)(c,d) 조건 (a-1,b)가 1이 아니어야
    if rot_num == 1:
        na, nb = a-1, b+1
        if check_boundary(na, nb, c, d) :
            if board[a-1][b] != 1 and check_visited(na, nb, c, d, ns):
                return (True, na, nb, c, d, ns)
            
    # (a,b)(c,d) -> (a,b)(c+1,d-1) 조건 (c+1,d)가 1이 아니어야
    if rot_num == 2:
        nc, nd = c+1, d-1
        if check_boundary(a, b, nc, nd) :
            if board[c+1][d] != 1 and check_visited(a, b, nc, nd, ns):
                return (True, a, b, nc, nd, ns)
            
    # (a,b)(c,d) -> (a,b)(c-1,d-1) 조건 (c-1,d)가 1이 아니어야
    if rot_num == 3:
        nc, nd = c-1, d-1
        if check_boundary(a, b, nc, nd) :
            if board[c-1][d] != 1 and check_visited(a, b, nc, nd, ns):
                return (True, a, b, nc, nd, ns)
            
    return (False, a, b, c, d, shape)
    
def bfs(board, a, b, c, d, shape):
    
    q = deque()
    q.append([a, b, c, d, shape, 0])
    # 가로 방향 (a,b) visited 처리
    visited[0][a][b] = True
    # 가로 방향 (c,d) visited 처리
    visited[0][c][d] = True
    
    while q:
        ca, cb, cc, cd, s, cnt = q.popleft()
        
        # 두개의 좌표중 하나가 (N-1,N-1)을 포함하는 경우 끝
        if (ca==N-1 and cb==N-1) or (cc == N-1 and cd == N-1):
            return cnt
        
        for d in range(4):
            na, nb, nc, nd = ca + dx[d], cb + dy[d], cc + dx[d], cd + dy[d]
            
            if check_boundary(na, nb, nc, nd):
                if board[na][nb] == 0 and board[nc][nd] == 0:
                    if check_visited(na, nb, nc, nd, s):
                        q.append([na, nb, nc, nd, s, cnt+1])
            
        for d in range(4):
            if s == 'v':
                go, na, nb, nc, nd, ns = rotation_v(d, board, ca, cb, cc, cd, s)
            else:
                go, na, nb, nc, nd, ns = rotation_h(d, board, ca, cb, cc, cd, s)
            if go == True and board[na][nb] == 0 and board[nc][nd] == 0:
            
                q.append([na, nb, nc, nd, ns, cnt+1])
    
    

def solution(board):
    global N, visited
    
    N = len(board[0])
    # visited[0][i][j] - 로봇이 가로로 놓여있을 때 방문 여부 체크
    # visited[1][i][j] - 로봇이 세로로 놓여있을 때 방문 여부 체크
    visited = [[[False]*N for i in range(N)] for k in range(2)]
    
    answer = bfs(board, 0, 0, 0, 1, 'h')
    # N*N 크기 지도 / 1*2 로봇
    # (0,0)(0,1) 부터 시작 -> 0 - 빈칸 / 1 - 벽
    
    return answer

