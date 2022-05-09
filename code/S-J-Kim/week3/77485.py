def solution(rows, columns, queries):
    answer = []
    board = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    for [x1, y1, x2, y2] in queries:

        htop = board[x1 - 1][y1 - 1 : y2 - 1]
        hbot = board[x2 - 1][y1:y2]

        vleft = [row[y1 - 1] for row in board[x1:x2]]
        vright = [row[y2 - 1] for row in board[x1 - 1 : x2 - 1]]

        answer.append(min(*htop, *hbot, *vleft, *vright))

        board[x1 - 1][y1:y2] = htop
        board[x2 - 1][y1 - 1 : y2 - 1] = hbot
        for (i, num) in zip(range(x1 - 1, x2), vleft):
            board[i][y1 - 1] = num

        for (i, num) in zip(range(x1, x2 + 1), vright):
            board[i][y2 - 1] = num

    return answer


solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
