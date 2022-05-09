import copy
import sys

sys.setrecursionlimit(10 ** 6)


def is_movable(loc, board):
    xloc = loc[1]
    yloc = loc[0]

    xlen = len(board[0])
    ylen = len(board)

    movable = False

    if xloc + 1 < xlen and board[yloc][xloc + 1]:
        movable = True

    if yloc + 1 < ylen and board[yloc + 1][xloc]:
        movable = True

    if xloc - 1 >= 0 and board[yloc][xloc - 1]:
        movable = True

    if yloc - 1 >= 0 and board[yloc - 1][xloc]:
        movable = True

    return movable


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def DFS(board, myloc, yourloc, moves):
    max_move = -1
    min_move = 9999999

    winnable = False

    if not is_movable(myloc, board):
        return [False, moves]

    if not board[myloc[0]][myloc[1]]:
        return [False, moves]

    for i in range(4):
        nx = myloc[1] + dx[i]
        ny = myloc[0] + dy[i]

        if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
            board[myloc[0]][myloc[1]] = 0
            res = DFS(board, yourloc, [ny, nx], moves + 1)
            board[myloc[0]][myloc[1]] = 1

            if not res[0]:
                # 상대방이 한번이라도 졌으면 -> 나는 이길 수 있는 방법이 있다 -> 무조건 최소 움직임으로 이기는 경우를 찾는다
                winnable = True
                min_move = min(min_move, res[1])

            elif not winnable:
                # 내가 한번도 이기지 못했으면 -> 어떻게는 제일 오래걸리는 경우를 찾는다
                max_move = max(max_move, res[1])

    return [winnable, min_move if winnable else max_move]


def solution(board, aloc, bloc):

    answer = DFS(board, aloc, bloc, 0)

    return answer[1]


solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4])
