def solution(board, skill):
    answer = 0
    prefixSum = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
 
    for type, r1, c1, r2, c2, degree in skill:
        prefixSum[r1][c1] += degree if type == 2 else -degree
        prefixSum[r1][c2 + 1] += -degree if type == 2 else degree
        prefixSum[r2 + 1][c1] += -degree if type == 2 else degree
        prefixSum[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    for i in range(len(prefixSum) - 1):
        for j in range(len(prefixSum[0]) - 1):
            prefixSum[i][j + 1] += prefixSum[i][j]

    for j in range(len(prefixSum[0]) - 1):
        for i in range(len(prefixSum) - 1):
            prefixSum[i + 1][j] += prefixSum[i][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += prefixSum[i][j]
            if board[i][j] > 0: answer += 1

    return answer
