import copy

def can_win(board, y1, x1, y2, x2):
    # (y1,x1)에 위치한 플레이어가 이길 수 있는지 여부와 최소횟수 계산
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    width = len(board[0])
    height = len(board)
    
    finished = True
    for i in range(4):
        if (0 <= y1 + dy[i] < height) and (0 <= x1 + dx[i] < width): # bound check
            if board[y1+dy[i]][x1+dx[i]]: # 바닥이 있음
                finished = False
    
    if finished:
        return (False, 0) # 이길 수 없고, 현재 위치 기준 0번 이동 가능
    elif x1 == x2 and y1 == y2:
        return (True, 1) # (y1,x1)에서 한 번 이동시 이길 수 있다
    
    minNum, maxNum = 99999, 0
    
    win = False # (y1,x1)에서 이동시 이기는 수가 단 하나라도 존재 하는가?
    for i in range(4):
        newY = y1 + dy[i]
        newX = x1 + dx[i]
        if (0 <= newY < height) and (0 <= newX < width): # bound check
            if board[newY][newX]:
                new_board = copy.deepcopy(board)
                new_board[y1][x1] = 0
                # can_win이 False라면 상대방이 이길 수 없는 것 => 내가 이기는 경우 반드시 존재
                opponent_win, count = can_win(new_board,y2,x2,newY,newX) # (y1,x1)과 (y2,x2) 위치 바꿔서 호출 (A<->B 턴 스위칭)
                if not opponent_win: # 상대가 진다 = 내가 이긴다
                    win = True
                    minNum = min(minNum, count) # 최소의 이동횟수 계산
                else: # 상대가 이긴다 = 내가 진다
                    maxNum = max(maxNum, count) # 최대한 오래 버티기위해 최대 이동횟수 계산
    count = minNum if win else maxNum
    return (win, count+1)
    
def solution(board, aloc, bloc):
    y1,x1 = aloc
    y2,x2 = bloc
    _, answer = can_win(board, y1,x1, y2,x2)
    
    return answer