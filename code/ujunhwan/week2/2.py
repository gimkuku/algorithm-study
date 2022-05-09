# 점찍어서?
def solution(*param):
    board, skill = param
    
    ans = 0
    row_max, col_max = len(board), len(board[0])
    
    psum = [[0 for col in range(col_max+1)] for row in range(row_max+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        degree = degree if type == 2 else -degree
        psum[r1][c1] += degree
        psum[r1][c2+1] += -degree
        psum[r2+1][c1] += -degree
        psum[r2+1][c2+1] += degree
    
    
    for col in range(col_max):
        for i in range(row_max):
            psum[i+1][col] += psum[i][col]
            
    for row in range(row_max):
        for i in range(col_max):
            psum[row][i+1] += psum[row][i]
    
    for row in range(row_max):
        for col in range(col_max):
            board[row][col] += psum[row][col]
            if board[row][col] >= 1:
                ans += 1
    
    return ans 