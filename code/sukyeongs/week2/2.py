def solution(board, skill):
    answer = 0
    
    for type, r1, c1, r2, c2, degree in skill:
        for y in range(r1, r2+1, 1):
            for x in range(c1, c2+1, 1):
                board[y][x] += degree if type == 2 else -degree 
    
    for row in board:
        answer += len(list(filter(lambda x: x > 0, row)))
    
    return answer
