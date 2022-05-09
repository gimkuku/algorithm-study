from collections import deque
from itertools import permutations, product
import copy

def out_of_range(y,x):
    return y < 0 or y >= 4 or x < 0 or x >= 4

def bfs(board, sy, sx, ey, ex):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    counts = [[-1]*4 for _ in range(4)]
    counts[sy][sx] = 0
    q = deque([(sy,sx)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            for press_ctrl in range(2):
                ny = y + dy[i]
                nx = x + dx[i]
                if press_ctrl: # 컨트롤 눌렀을 때
                    while True:
                        if out_of_range(ny,nx):
                            ny -= dy[i]
                            nx -= dx[i]
                            break
                        if board[ny][nx] > 0:
                            break
                        ny += dy[i]
                        nx += dx[i]
                    if counts[ny][nx] == -1:
                        q.append((ny,nx))
                        counts[ny][nx] = counts[y][x] + 1
                        if ny == ey and nx == ex: # 만약 (ey,ex)에 도달했으면 탈출
                            return counts[ny][nx]
                else: # 컨트롤 안눌렀을 때
                    if not out_of_range(ny,nx):
                        if counts[ny][nx] == -1:
                            q.append((ny,nx))
                            counts[ny][nx] = counts[y][x] + 1
                            if ny == ey and nx == ex: # 만약 (ey,ex)에 도달했으면 탈출
                                return counts[ny][nx]
    return counts[ey][ex]

def solution(board, r, c):
    answer = int(1e9)
    cards = [[],[],[],[],[],[],[]] # cards[i]에 i번 카드 두 개의 좌표 존재
    cards_nums = []
    for y in range(4):
        for x in range(4):
            if 1 <= board[y][x] <= 6:
                cards[board[y][x]].append((y,x))
                cards_nums.append(board[y][x])
    cards_nums = list(set(cards_nums)) # 존재하는 카드 숫자들
    saved_board = copy.deepcopy(board) # 보드 초기 상태

		# 처리할 카드 순서
    for cards_perm in permutations(cards_nums, len(cards_nums)):
				# 두 개의 카드 중 0 또는 1번쨰 부터 처리
        for start_idx in product([0,1], repeat=len(cards_nums)):
            count = 0
            y = r
            x = c
            for i in range(len(cards_nums)):
                card_num = cards_perm[i]
                curr = start_idx[i] # 0 또는 1
                first_y, first_x = cards[card_num][curr]
                second_y, second_x = cards[card_num][(curr+1)%2]
                
                # 첫번째 카드 삭제
                count += bfs(board, y, x, first_y, first_x) + 1
                board[first_y][first_x] = 0
                if count > answer: # 만약 계산 중간이 최솟값보다 크면 break
                    break
                    
                # 두번째 카드 삭제
                count += bfs(board, first_y, first_x, second_y, second_x) + 1
                board[second_y][second_x] = 0
                if count > answer: # 만약 계산 중간이 최솟값보다 크면 break
                    break
                
                # 현재 위치 갱신
                y = second_y
                x = second_x
            answer = min(answer, count)
            # board 복구
            for y in range(4):
                for x in range(4):
                    board[y][x] = saved_board[y][x]
          
    return answer