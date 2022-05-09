def solution(board, aloc, bloc):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    
    MAX_Y = len(board)
    MAX_X = len(board[0])
    
    def isValid(ny, nx):
        if ny < 0 or nx < 0 or ny >= MAX_Y or nx >= MAX_X:
            return False
        return True
    
    # ret = win, count
    # count odd -> B
    def dfs(aPos, bPos, count):
        ay, ax = aPos
        by, bx = bPos
        
        isPossible = False
        maxval, minval = count, 1000
        
        canWin = False
        
        # b turn
        if count & 1:
            if board[by][bx] == 0:
                return (0, count)
            
            for k in range(4):
                ny, nx = by + dy[k], bx + dx[k]
                if isValid(ny, nx) and board[ny][nx] == 1:
                    isPossible = True
                    board[by][bx] = 0
                    
                    # win -> par node win = cur node lose
                    # par node lose = cur node win
                    win, result = dfs(aPos, [ny, nx], count+1)
                    board[by][bx] = 1
                    
                    if win == 0:
                        canWin = True
                        minval = min(minval, result)
                    else:
                        maxval = max(maxval, result)
                    
        else:
            if board[ay][ax] == 0:
                return (0, count)
            
            for k in range(4):
                ny, nx = ay + dy[k], ax + dx[k]
                if isValid(ny, nx) and board[ny][nx] == 1:
                    isPossible = True
                    board[ay][ax] = 0
                    win, result = dfs([ny, nx], bPos, count+1)
                    board[ay][ax] = 1
                    
                    if win == 0:
                        canWin = True
                        minval = min(minval, result)
                    else:
                        maxval = max(maxval, result)
                        
        if not isPossible:
            return (0, count)
        if canWin:
            return (1, minval)
        return (0, maxval)
    
    ans = dfs(aloc, bloc, 0)[1]
    return ans