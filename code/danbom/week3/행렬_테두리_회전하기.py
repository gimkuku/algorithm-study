def make_board(rows, columns):
    board = [[1 for col in range(columns)] for row in range(rows)]
    index = 0
    for row in range(rows):
        for col in range(columns):
            board[row][col] += index
            index += 1
    return board

def get_mins(board, queries):
    result = []
    
    for x1,y1,x2,y2 in queries:
        x1 -= 1
        y1 -= 1 
        x2 -= 1
        y2 -= 1
        start = board[x1][y1]
        _min = [start]

        # (y1열) x2행 -> x1행 방향 회전
        for i in range(x1,x2,1):
            temp = board[i+1][y1]
            board[i][y1] = temp
            _min.append(temp)
            
        # (x2행) y2열 -> y1열 방향 회전
        for i in range(y1,y2,1):
            temp = board[x2][i+1]
            board[x2][i] = temp
            _min.append(temp)
            
        # (y2열) x1행 -> x2행 방향 회전
        for i in range(x2,x1,-1):
            temp = board[i-1][y2]
            board[i][y2] = temp
            _min.append(temp)
            
        # (x1행) y1열 -> y2열 방향 회전
        for i in range(y2,y1,-1):
            temp = board[x1][i-1]
            board[x1][i] = temp
            _min.append(temp)
            
        board[x1][y1+1] = start
        result.append(min(_min))
        
    return result
            
def solution(rows, columns, queries):
    board = make_board(rows, columns)
    return get_mins(board, queries)
