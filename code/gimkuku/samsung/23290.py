from copy import deepcopy

def solution(m, p, board, sx, sy):
    # 상어 방향 : 상 1, 좌 2, 하 3, 우 4
    sdirs = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                sdirs.append([i, j, k])
    sd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 물고기 방향
    dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    # 물고기 냄새
    smell = [[0 for i in range(4)] for j in range(4)]
    
    # print("\n시작")
    # for i in range(4):
    #     print(board[i])

    for _p in range(p):
        answer = 0
        # for i in range(4):
        #     print(board[i])
        # print(answer)
        # print("물고기 냄새",smell)
        # 이전 물고기 복사
        prev = deepcopy(board)
        move = []
        # 이동할 물고기 체크
        for x in range(4):
            for y in range(4):
                # 그 자리에 물고기가 있으면
                if board[x][y].count(0) != 8:
                    for fish in range(8):
                        for repeat in range(8):
                            d = (fish - repeat + 8) % 8
                            dx, dy = dirs[d]
                            if x + dx < 0 or y + dy < 0 or x + dx > 3 or y + dy > 3: continue
                            if x + dx == sx and y + dy == sy: continue
                            if smell[x + dx][y + dy]: continue
                            cnt = board[x][y][fish]
                            move.append([x + dx, y + dy, d, cnt])
                            board[x][y][fish] = 0
                            break
  
        
        # 물고기 이동
        for nx, ny, nd,cnt in move:
            board[nx][ny][nd] += cnt
        
        # print("물고기 이동!!")
        # for i in range(4):
        #     print(board[i])
        # 상어 이동
        _max = 0
        _maxfish = []
        _maxshark = (sx, sy)

        # 64가지 방법 중
        # print("상어 위치", sx," ,",sy)
        for _sdirs in sdirs:
            eat = 0
            fishes = []
            # 상어 위치 원래대로
            _sx, _sy = sx, sy
            flag = True
            # 세 방향으로 이동시키기
            for num in _sdirs:
                dx, dy = sd[num]
                if _sx + dx < 0 or _sy + dy < 0 or _sx + dx > 3 or _sy + dy > 3:
                    flag = False
                    break
                # 상어 이동
                _sx = _sx + dx
                _sy = _sy + dy
                if (_sx, _sy) not in fishes:
                    for k in range(8):
                        eat += board[_sx][_sy][k]
                fishes.append((_sx, _sy))

            # 물고기 젤 많이 먹었을 때 
            if eat >= _max and flag:
                _maxshark = (_sx, _sy)
                _max = eat
                _maxfish = fishes
        
        # print("상어 이동경로", _maxfish)
        # print("상어 먹은 양", _max)

        # 제일 많이 먹는 방법 찾았으면 상어 이동
        for x, y in _maxfish:
            if board[x][y].count(0) != 8:
                smell[x][y] = _p + 2
            board[x][y] = [0, 0, 0, 0, 0, 0, 0, 0]
            
        # 상어 위치 업데이트
        sx, sy = _maxshark

        # 냄새 제거
        for x in range(4):
            for y in range(4):
                if smell[x][y] == _p:
                    smell[x][y] = 0
        # print("\n",_p,"번 연습 끝 + 복제 전")
        # for i in range(4):
        #     print(board[i])
        # print("\n")

        # 복제 마법
        # print("board\n",board)
        for x in range(4):
            for y in range(4):
                for k in range(8):
                    board[x][y][k] += prev[x][y][k]
        
        # print("\n",_p,"번 연습 끝")
        # for i in range(4):
        #     print(board[i])
        # print("\n")
    answer = 0
    for i in range(4):
        for j in range(4):
            for k in range(8):
                answer += board[i][j][k]
    print(answer)
                            



m, p = map(int, input().split())
board = [[[0 for k in range(8)] for i in range(4)] for j in range(4)]

for i in range(m):
    x, y, d = map(int, input().split())
    board[x - 1][y - 1][d - 1] += 1

sx, sy = map(int, input().split())

solution(m, p, board, sx -1, sy -1)