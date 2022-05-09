from collections import deque

def solution(board):
    n = len(board)
    # 회전 4방향 - 가로일 때 왼쪽이 x1y1 오른쪽이 x2y2
    r_h_dirs = [[[1, 0, 0, 0], [0, 1, 0, 0]], [[0, 0, 1, 0], [0, 0, 0, -1]], [[-1, 0, 0, 0], [0, 1, 0, 0]], [[0, 0, -1, 0], [0, 0, 0, -1]]]
    # 회전 4방향 - 세로일 때 위가 x1y1 아래가 x2y2
    r_v_dirs = [[[0, 0, 0, 1], [0, 0, -1, 0]], [[0, 0, 0, -1], [0, 0, -1, 0]], [[0, 1, 0, 0], [1, 0, 0, 0]], [[0, -1, 0, 0], [1, 0, 0, 0]]]
    s_dirs = [[[-1, 0, -1, 0]], [[1, 0, 1, 0]], [[0, -1, 0, -1]], [[0, 1, 0, 1]]]
    
    x1,y1 = 0,0
    x2,y2 = 0,1
    q = deque([[x1,y1,x2,y2,[[x1,y1,x2,y2]]]])
    flag = 10
    while q:
        _x1, _y1, _x2, _y2, _path = q.popleft()
        if flag:
            print("---")
            print(_path)
            print("\n")
            flag -= 1
        if (_x1 == n - 1 and _y1 == n - 1) or (_x2 == n - 1 and _y2 == n - 1):
            print(_path, len(_path))
            return len(_path) -1
        vert, hori = False , False
        # 방향 결정
        # print(_path)
        if (_x1 == _x2): hori = True
        if (_y1 == _y2): vert = True
        
        
            
                
        if vert:
            for d in r_v_dirs:
                if _y1 > _y2 : x1, y1, x2, y2 = _x2, _y2, _x1, _y1
                else : x1, y1, x2, y2 = _x1, _y1, _x2, _y2
                path = _path[:]
                flag = True
                # 회전하는 경우는 두번 움직여야 돼
                for dx1, dy1, dx2, dy2 in d:
                    # 밖으로 나간 경우
                    if ( x1 + dx1 < 0 or x1 + dx1 > n-1 or
                        x2 + dx2 < 0 or x2 + dx2 > n-1 or
                        y1 + dy1 < 0 or y1 + dy1 > n-1 or
                        y2 + dy2 < 0 or y2 + dy2 > n - 1):
                        flag = False
                        break
                    # 벽인 경우
                    if (board[x1 + dx1][y1 + dy1] == 1 or
                    board[x2 + dx2][y2 + dy2] == 1):
                        flag = False
                        break
                    x1, y1, x2, y2 = x1 + dx1, y1 + dy1, x2 + dx2, y2 + dy2
                    if [x1, y1, x2, y2] in path:
                        flag = False
                        break
                # 갈 수 있으면
                if flag:
                    path += [[x1,y1,x2,y2]]
                    q.append([x1,y1,x2,y2,path])
        
        if hori:
            for d in r_h_dirs:
                path = _path[:]
                flag = True
                if _x1 > _x2 : x1, y1, x2, y2 = _x2, _y2, _x1, _y1
                else : x1, y1, x2, y2 = _x1, _y1, _x2, _y2
                # 회전하는 경우는 두번 움직여야 돼
                for dx1, dy1, dx2, dy2 in d:
                    # 밖으로 나간 경우
                    if ( x1 + dx1 < 0 or x1 + dx1 > n-1 or
                        x2 + dx2 < 0 or x2 + dx2 > n-1 or
                        y1 + dy1 < 0 or y1 + dy1 > n-1 or
                        y2 + dy2 < 0 or y2 + dy2 > n - 1):
                        flag = False
                        break
                    # 벽인 경우
                    if (board[x1 + dx1][y1 + dy1] == 1 or
                        board[x2 + dx2][y2 + dy2] == 1):
                        flag = False
                        break
                    x1, y1, x2, y2 = x1 + dx1, y1 + dy1, x2 + dx2, y2 + dy2
                    if [x1, y1, x2, y2] in path:
                        flag = False
                        break
                # 갈 수 있으면
                if flag:
                    path += [[x1,y1,x2,y2]]
                    q.append([x1, y1, x2, y2, path])

        # 직진
        for d in s_dirs:
            x1, y1, x2, y2 = _x1, _y1, _x2, _y2
            path = _path[:]
            flag = True
            # 회전하는 경우는 두번 움직여야 돼
            for dx1, dy1, dx2, dy2 in d:
                # 밖으로 나간 경우
                if ( x1 + dx1 < 0 or x1 + dx1 > n-1 or
                    x2 + dx2 < 0 or x2 + dx2 > n-1 or
                    y1 + dy1 < 0 or y1 + dy1 > n-1 or
                    y2 + dy2 < 0 or y2 + dy2 > n - 1):
                    flag = False
                    break
                # 벽인 경우
                if (board[x1 + dx1][y1 + dy1] == 1 or
                    board[x2 + dx2][y2 + dy2] == 1):
                    flag = False
                    break
                x1, y1, x2, y2 = x1 + dx1, y1 + dy1, x2 + dx2, y2 + dy2
                if [x1, y1, x2, y2] in path:
                    flag = False
                    break
            # 갈 수 있으면
            if flag:
                path += [[x1,y1,x2,y2]]
                q.append([x1, y1, x2, y2, path])
                    
solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]])