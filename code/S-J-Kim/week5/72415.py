from copy import deepcopy
from itertools import permutations
from collections import deque


minval = 999999999

board = []


def solution(input_board, sr, sc):
    global board
    board = input_board
    location = [[] for _ in range(7)]
    nums = []

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if board[i][j] not in nums:
                    nums.append(board[i][j])
                location[board[i][j]].append((i, j))

    per = list(permutations(nums, len(nums)))  # 순열
    answer = float("inf")

    for i in range(len(per)):
        board = deepcopy(input_board)  # 지웠던 곳 다시 채우기
        cnt = 0
        r, c = sr, sc

        for j in per[i]:
            left = bfs((r, c), location[j][0])
            right = bfs((r, c), location[j][1])

            if left < right:
                cnt += left
                cnt += bfs(location[j][0], location[j][1])
                r, c = location[j][1]

            else:
                cnt += right
                cnt += bfs(location[j][1], location[j][0])
                r, c = location[j][0]

            board[location[j][0][0]][location[j][0][1]] = 0  # 카드 지우기
            board[location[j][1][0]][location[j][1][1]] = 0  # 카드 지우기

            cnt += 2  # enter

        answer = min(answer, cnt)
    return answer


def ctrl(r, c, dr, dc):
    global board

    cr, cc = r, c

    while True:
        nr = cr + dr
        nc = cc + dc

        if not (0 <= nr < 4 and 0 <= nc < 4):
            return (cr, cc)

        if board[nr][nc]:
            return (nr, nc)

        cr = nr
        cc = nc


def bfs(src, dst):
    r, c = src
    gr, gc = dst

    q = deque()
    q.append((r, c, 0))

    visited = [[False] * 4 for _ in range(4)]
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while q:
        r, c, cost = q.popleft()

        if visited[r][c]:
            continue
        visited[r][c] = True

        if (r, c) == (gr, gc):
            return cost

        for dr, dc in move:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < 4 and 0 <= nc < 4:
                q.append((nr, nc, cost + 1))

            nr, nc = ctrl(r, c, dr, dc)
            q.append((nr, nc, cost + 1))

    return -1


solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)

"""
우선 카드 좌표 모음에 대해서 순열 구함

카드가 두개 있으니까 각각 먼저 가보게 하고 먼저 도착하는걸 고름
다음 카드 볼 때 반복
"""
