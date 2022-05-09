def solution(rows, columns, queries):
    global board
    board = [[0 for col in range(columns)] for row in range(rows)]
    k = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = k
            k += 1
    
    def rotate(start, end):
        global board
        x1, y1 = start
        x3, y3 = end
        x2, y2 = x3, y1
        x4, y4 = x1, y3
        
        sVal = board[y1][x2]
        
        minval = 987654321
        
        for j in range(x2, x1, -1):
            board[y1][j] = board[y1][j-1]
            minval = min(minval, board[y1][j])
            
        for i in range(y1, y3):
            board[i][x1] = board[i+1][x1]
            minval = min(minval, board[i][x1])
            
        for j in range(x1, x3):
            board[y3][j] = board[y3][j+1]
            minval = min(minval, board[y3][j])
            
        for i in range(y3, y1, -1):
            board[i][x3] = board[i-1][x3]
            minval = min(minval, board[i][x3])
            
        board[y1+1][x2] = sVal
        
        minval = min(minval, sVal)
            
        return minval

    answer = []
    
    for y1, x1, y2, x2 in queries:
        answer.append(rotate([x1-1, y1-1], [x2-1, y2-1]))
    
    print(answer)
    return answer