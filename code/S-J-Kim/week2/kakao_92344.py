def solution(board, skill):
    answer = 0
    acc_map = [[0 for j in range(len(board[i]))] for i in range(len(board))]

    BOUND_X = len(board[0]) - 1
    BOUND_Y = len(board) - 1

    for command in skill:
        s_type, r1, c1, r2, c2, degree = command

        if s_type == 1:
            degree = -degree

        acc_map[r1][c1] += degree

        if r2 < BOUND_Y:
            acc_map[r2 + 1][c1] -= degree

        if c2 < BOUND_X:
            acc_map[r1][c2 + 1] -= degree

        if r2 < BOUND_Y and c2 < BOUND_X:
            acc_map[r2 + 1][c2 + 1] += degree

    for i in range(BOUND_Y + 1):
        for j in range(1, BOUND_X + 1):
            acc_map[i][j] += acc_map[i][j - 1]

    for j in range(BOUND_X + 1):
        for i in range(1, BOUND_Y + 1):
            acc_map[i][j] += acc_map[i - 1][j]

    for i in range(BOUND_Y + 1):
        for j in range(BOUND_X + 1):
            board[i][j] += acc_map[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


solution(
    [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
    [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]],
)
