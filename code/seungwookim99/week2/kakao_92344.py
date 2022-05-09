def solution(board, skill):
    answer = 0
    height, width = len(board), len(board[0])
    matrix = [[0] * (width+1) for _ in range(height+1)] # (height+1) x (width+1) matrix

    # 시작 좌표, 끝 좌표 기록 : O(len(skill))
    for type, r1, c1, r2, c2, degree in skill:
        degree *= (-1) if type == 1 else 1
        matrix[r1][c1] += degree
        matrix[r2+1][c2+1] += degree
        matrix[r1][c2+1] -= degree
        matrix[r2+1][c1] -= degree
        
    # 누적 합 계산 : O(width*height)
    # 가로 방향 (좌->우) 누적합 계산
    for i in range(1,width+1):
        for j in range(height+1):
            matrix[j][i] += matrix[j][i-1]
    
    # 세로 방향 (상->하) 누적합 계산
    for j in range(1,height+1):
        for i in range(width+1):
            matrix[j][i] += matrix[j-1][i]
    
    # 파괴되지 않은 건물 개수 계산
    for y in range(height):
        for x in range(width):
            if board[y][x] + matrix[y][x] > 0 :
                answer += 1
    return answer