from collections import defaultdict, deque
from itertools import permutations

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
_min = float('inf')

def solution(board, r, c):
    global _min
    dic = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dic[board[i][j]].append((i, j))

    def get_dist(r1, c1, r2, c2):
        dist = [[20] * 4 for _ in range(4)]
        dist[r1][c1] = 0

        queue = deque([(r1, c1)])

        while queue:
            rr, cc = queue.popleft()
            for dr, dc in move:
                for i in range(1, 4):
                    nr, nc = rr + dr * i, cc + dc * i
                    if 0 <= nr < 4 and 0 <= nc < 4 and dist[nr][nc] >= dist[rr][cc] + 1:
                        if (nr, nc) == (r2, c2):
                            return dist[rr][cc] + 1
                        if board[nr][nc] != 0 and check[board[nr][nc]] == 0 or dr == 1 and nr == 3 or dr == -1 and nr == 0 or dc == 1 and nc == 3 or dc == -1 and nc == 0:
                            dist[nr][nc] = dist[rr][cc] + 1
                            queue.append((nr, nc))
                            break
            for dr, dc in move:
                nr, nc = rr + dr, cc + dc
                if 0 <= nr < 4 and 0 <= nc < 4 and dist[nr][nc] >= dist[rr][cc] + 1:
                    dist[nr][nc] = dist[rr][cc] + 1
                    queue.append((nr, nc))

        return dist[r2][c2]

    def dfs(v, now_r, now_c, s):
        global _min
        if s >= _min:
            return
        if v >= len(dic):
            _min = min(_min, s)
            return
        else:
            start, end = dic[order[v]]
            r1, c1 = start
            r2, c2 = end

            check[board[r1][c1]] = 1
            dfs(v + 1, r1, c1, s + get_dist(now_r, now_c, r2, c2) + get_dist(r2, c2, r1, c1) + 2)
            dfs(v + 1, r2, c2, s + get_dist(now_r, now_c, r1, c1) + get_dist(r1, c1, r2, c2) + 2)
            check[board[r2][c2]] = 0

    for order in permutations(dic.keys()):
        check = [0] + [1] * 8

        for key in dic.keys():
            check[key] = 0

        dfs(0, r, c, 0)

    return _min
