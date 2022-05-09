import copy

def A_func(board,aloc,bloc,total_move):
        a_x,a_y = aloc

        if board[a_x][a_y] == 0:
            result = [False,total_move]
            return result

        cango = False 
        canwin = [] 
        nowin = [] 

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            next_x = a_x + dx[i]
            next_y = a_y + dy[i]

            if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
                if board[next_x][next_y] == 1:
                    next_board = copy.deepcopy(board)
                    next_board[a_x][a_y] = 0
                    b_win,cnt_move = B_func(next_board,(next_x,next_y),bloc,total_move+1)
                    if b_win == False:
                        canwin.append(cnt_move)
                    else:
                        nowin.append(cnt_move)
                    cango = True

        if cango:
            if canwin:
                result = [True, min(canwin)]
            else:
                result = [False,max(nowin)]

        else:
            result = [False,total_move]

        return result
    
def B_func(board,aloc,bloc,total_move):
    b_x,b_y = bloc
    
    if board[b_x][b_y] == 0:
        result = [False,total_move]
        return result
    
    cango = False
    canwin = []
    nowin = []
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        next_x = b_x + dx[i]
        next_y = b_y + dy[i]
        
        if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
            
            if board[next_x][next_y] == 1:
                next_board = copy.deepcopy(board)
                next_board[b_x][b_y] = 0
                a_win,cnt_move = A_func(next_board,aloc,(next_x,next_y),total_move+1)
                if a_win == False:
                    canwin.append(cnt_move)
                else:
                    nowin.append(cnt_move)
                cango = True
                
    if cango:
        if canwin:
            result = True,min(canwin)
        else:
            result = False,max(nowin)
    else:
        result = False,total_move
    
    return result

def solution(board, aloc, bloc):
    return A_func(board,aloc,bloc,0)[1]
