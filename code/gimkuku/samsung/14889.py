from itertools import combinations
def calc(member):
    global board
    value = 0
    for i in member:
        for j in member:
            value += board[i][j]
    return value
    
def solution(n, _board):
    answer = float('inf')
    global board
    board = _board
    member = [i for i in range(n)]
    member_comb = list(map(set, combinations(member, n // 2)))
    for i in member_comb[:len(member_comb)//2]:
        member1 = i
        member2 = set(member) - set(i)
        c1 = calc(member1)
        c2 = calc(member2)
        value = max(c1, c2) - min(c1, c2)
        if value < answer:
            answer = value
    print(answer)

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    
solution(n,board)