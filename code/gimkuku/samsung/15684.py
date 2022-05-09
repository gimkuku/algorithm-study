from itertools import combinations
from copy import deepcopy
def solution(n, m, h, lines):
    board = [[0 for j in range(n-1)] for i in range(h)]
    for i in lines:
        _h, _n = i
        board[_h - 1][_n - 1] = 1
    # print(board)
    zero_list = []

    for i in range(h):
        for j in range(n-1):
            if board[i][j] == 0:
                zero_list.append(j*h+i)

    # 사다리가 될수 있는 모든 경우 구하기
    sadari = [[]]
    for _sadaricnt in range(4):
        sadari = list(map(list, combinations(zero_list, _sadaricnt)))
        for check in sadari:
            flag = False
            # 사다리 체크
            for j in check:
                _n, _h = j // h, j % h
                if _n -1 >= 0:
                    if board[_h][_n - 1] == 1:
                        flag = True
                        break
                if _n + 1 < n - 1:
                    if board[_h][_n + 1] == 1:
                        flag = True
                        break
            if flag:
                continue

            # 사다리 설치
            b = board[:]
            for j in check:
                _n, _h = j // h, j % h
                b[_h][_n] = 1
            
            # 0번부터 사다리 내려가기
            for i in range(n):
                now = 0
                value = i

                # 사다리 타기 시작
                while True:
                    # 다 내려왔음 멈추기
                    if now == h:
                        break
                    # 오른쪽으로 이동
                    if value < n-1:
                        if b[now][value] == 1:
                            value += 1
                            now += 1
                            continue
                    # 왼쪽으로 이동
                    if (value -1) > -1:
                        if b[now][value - 1] == 1:
                            value -= 1
                            now += 1
                            continue
                    now += 1
                    
                # 돌아온 값이 i 가 아니면 실패
                if value != i:
                    break
                elif value == n - 1:
                    print(_sadaricnt)
                    return

            for j in check:
                _n, _h = j // h, j % h
                b[_h][_n] = 0
    print(-1)

n, m, h = map(int, input().split())
lines = []
for i in range(m):
    lines.append(list(map(int, input().split())))
solution(n,m,h,lines)