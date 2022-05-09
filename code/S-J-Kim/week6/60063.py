from collections import deque


def get_movable_points(pos1, pos2, board):
    candidates = []

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # horizontal move
    for i in range(4):
        np1 = (pos1[0] + dy[i], pos1[1] + dx[i])
        np2 = (pos2[0] + dy[i], pos2[1] + dx[i])

        if not (board[np1[0]][np1[1]] or board[np2[0]][np2[1]]):
            candidates.append((np1, np2))

    # rotation move
    delta = [-1, 1]

    # case1: block aligned hoziontally
    if pos1[0] == pos2[0]:
        for nxt in delta:
            np1 = (pos1[0] + nxt, pos1[1])
            np2 = (pos2[0] + nxt, pos2[1])

            if not (board[np1[0]][np1[1]] or board[np2[0]][np2[1]]):
                candidates.append((pos1, np1))
                candidates.append((pos2, np2))

    # case2: block aligned vertically
    else:
        for nxt in delta:
            np1 = (pos1[0], pos1[1] + nxt)
            np2 = (pos2[0], pos2[1] + nxt)

            if not (board[np1[0]][np1[1]] or board[np2[0]][np2[1]]):
                candidates.append((np1, pos1))
                candidates.append((np2, pos2))

    return candidates


def solution(board):
    goal = len(board)
    nboard = [[1 for _ in range(len(board[0]) + 2)] for __ in range(len(board) + 2)]

    # add padding
    for i in range(len(board)):
        for j in range(len(board[0])):
            nboard[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = set([])

    q.append([(1, 1), (1, 2), 0])
    visited.add(((1, 1), (1, 2)))

    while q:
        pos1, pos2, cost = q.popleft()

        if pos1 == (goal, goal) or pos2 == (goal, goal):
            return cost

        next_move = get_movable_points(pos1, pos2, nboard)

        for move in next_move:
            if move not in visited:
                q.append((*move, cost + 1))
                visited.add(move)


solution(
    [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]
)

# board에 대해서, 평행이동이 가능한 좌표들, 회전이동이 가능한 좌표를 리턴
# 큐 돌면서 타겟 좌표 나오는 순간에 그때의 값 리턴
