from copy import deepcopy
def rotate_1(dir, board):
    dirs = ['','U','D','F','B','L','R']
    now = dirs.index(dir[0])
    if dir[1] == '+':
        temp1 = board[now][0]
        board[now][0] = board[now][6]
        board[now][6] = board[now][8]
        board[now][8] = board[now][2]
        board[now][2] = temp1
        
        temp2 = board[now][1]
        board[now][1] = board[now][3]
        board[now][3] = board[now][7]
        board[now][7] = board[now][5]
        board[now][5] = temp2

    elif dir[1] == '-':
        temp1 = board[now][0]
        board[now][0] = board[now][2]
        board[now][2] = board[now][8]
        board[now][8] = board[now][6]
        board[now][6] = temp1
 
        temp2 = board[now][1]
        board[now][1] = board[now][5]
        board[now][5] = board[now][7]
        board[now][7] = board[now][3]
        board[now][3] =temp2

def rotate_2(dir, board):
    if dir == 'U+':
        temp1 = board[6][0]
        temp2 = board[6][1]
        temp3 = board[6][2]
        board[6][0] = board[4][0]
        board[6][1] = board[4][1]
        board[6][2] = board[4][2]
        board[4][0] = board[5][0]
        board[4][1] = board[5][1]
        board[4][2] = board[5][2]
        board[5][0] = board[3][0]
        board[5][1] = board[3][1]
        board[5][2] = board[3][2]
        board[3][0] = temp1
        board[3][1] = temp2
        board[3][2] = temp3

    elif dir == 'U-':
        temp1 = board[6][0]
        temp2 = board[6][1]
        temp3 = board[6][2]
        board[6][0] = board[3][0]
        board[6][1] = board[3][1]
        board[6][2] = board[3][2]
        board[3][0] = board[5][0]
        board[3][1] = board[5][1]
        board[3][2] = board[5][2]
        board[5][0] = board[4][0]
        board[5][1] = board[4][1]
        board[5][2] = board[4][2]
        board[4][0] = temp1
        board[4][1] = temp2
        board[4][2] = temp3
    elif dir == 'D+':
        temp1 = board[3][6]
        temp2 = board[3][7]
        temp3 = board[3][8]
        board[3][6] = board[5][6]
        board[3][7] = board[5][7]
        board[3][8] = board[5][8]
        board[5][6] = board[4][6]
        board[5][7] = board[4][7]
        board[5][8] = board[4][8]
        board[4][6] = board[6][6]
        board[4][7] = board[6][7]
        board[4][8] = board[6][8]
        board[6][6] = temp1
        board[6][7] = temp2
        board[6][8] = temp3
    elif dir == 'D-':
        temp1 = board[3][6]
        temp2 = board[3][7]
        temp3 = board[3][8]
        board[3][6] = board[6][6]
        board[3][7] = board[6][7]
        board[3][8] = board[6][8]
        board[6][6] = board[4][6]
        board[6][7] = board[4][7]
        board[6][8] = board[4][8]
        board[4][6] = board[5][6]
        board[4][7] = board[5][7]
        board[4][8] = board[5][8]
        board[5][6] = temp1
        board[5][7] = temp2
        board[5][8] = temp3
    elif dir == 'F+':
        temp1 = board[1][6]
        temp2 = board[1][7]
        temp3 = board[1][8]
        board[1][6] = board[5][8]
        board[1][7] = board[5][5]
        board[1][8] = board[5][2]
        board[5][8] = board[2][2]
        board[5][5] = board[2][1]
        board[5][2] = board[2][0]
        board[2][2] = board[6][0]
        board[2][1] = board[6][3]
        board[2][0] = board[6][6]
        board[6][0] = temp1
        board[6][3] = temp2
        board[6][6] = temp3
    elif dir == 'F-':
        temp1 = board[1][6]
        temp2 = board[1][7]
        temp3 = board[1][8]
        board[1][6] = board[6][0]
        board[1][7] = board[6][3]
        board[1][8] = board[6][6]
        board[6][0] = board[2][2]
        board[6][3] = board[2][1]
        board[6][6] = board[2][0]
        board[2][2] = board[5][8]
        board[2][1] = board[5][5]
        board[2][0] = board[5][2]
        board[5][8] = temp1
        board[5][5] = temp2
        board[5][2] = temp3
    elif dir == 'B+':
        temp1 = board[1][0]
        temp2 = board[1][1]
        temp3 = board[1][2]
        board[1][0] = board[6][2]
        board[1][1] = board[6][5]
        board[1][2] = board[6][8]
        board[6][2] = board[2][8]
        board[6][5] = board[2][7]
        board[6][8] = board[2][6]
        board[2][8] = board[5][6]
        board[2][7] = board[5][3]
        board[2][6] = board[5][0]
        board[5][6] = temp1
        board[5][3] = temp2
        board[5][0] = temp3
    elif dir == 'B-':
        temp1 = board[1][0]
        temp2 = board[1][1]
        temp3 = board[1][2]
        board[1][0] = board[5][6]
        board[1][1] = board[5][3]
        board[1][2] = board[5][0]
        board[5][6] = board[2][8]
        board[5][3] = board[2][7]
        board[5][0] = board[2][6]
        board[2][8] = board[6][2]
        board[2][7] = board[6][5]
        board[2][6] = board[6][8]
        board[6][2] = temp1
        board[6][5] = temp2
        board[6][8] = temp3
    elif dir == 'L+':
        temp1 = board[3][0]
        temp2 = board[3][3]
        temp3 = board[3][6]
        board[3][0] = board[1][0]
        board[3][3] = board[1][3]
        board[3][6] = board[1][6]
        board[1][0] = board[4][8]
        board[1][3] = board[4][5]
        board[1][6] = board[4][2]
        board[4][8] = board[2][0]
        board[4][5] = board[2][3]
        board[4][2] = board[2][6]
        board[2][0] = temp1
        board[2][3] = temp2
        board[2][6] = temp3
    elif dir == 'L-':
        temp1 = board[3][0]
        temp2 = board[3][3]
        temp3 = board[3][6]
        board[3][0] = board[2][0]
        board[3][3] = board[2][3]
        board[3][6] = board[2][6]
        board[2][0] = board[4][8]
        board[2][3] = board[4][5]
        board[2][6] = board[4][2]
        board[4][8] = board[1][0]
        board[4][5] = board[1][3]
        board[4][2] = board[1][6]
        board[1][0] = temp1
        board[1][3] = temp2
        board[1][6] = temp3
    elif dir == 'R+':
        temp1 = board[3][2]
        temp2 = board[3][5]
        temp3 = board[3][8]
        board[3][2] = board[2][2]
        board[3][5] = board[2][5]
        board[3][8] = board[2][8]
        board[2][2] = board[4][6]
        board[2][5] = board[4][3]
        board[2][8] = board[4][0]
        board[4][6] = board[1][2]
        board[4][3] = board[1][5]
        board[4][0] = board[1][8]
        board[1][2] = temp1
        board[1][5] = temp2
        board[1][8] = temp3
    elif dir == 'R-':
        temp1 = board[3][2]
        temp2 = board[3][5]
        temp3 = board[3][8]
        board[3][2] = board[1][2]
        board[3][5] = board[1][5]
        board[3][8] = board[1][8]
        board[1][2] = board[4][6]
        board[1][5] = board[4][3]
        board[1][8] = board[4][0]
        board[4][6] = board[2][2]
        board[4][3] = board[2][5]
        board[4][0] = board[2][8]
        board[2][2] = temp1
        board[2][5] = temp2
        board[2][8] = temp3

    

def solution(testcase, rule):
    board = [[]]
    board.append(['w'] * 9) # 윗면
    board.append(['y'] * 9) # 아랫면
    board.append(['r'] * 9) # 앞면
    board.append(['o'] * 9) # 뒷면
    board.append(['g'] * 9) # 왼면
    board.append(['b'] * 9) # 오른면

    answer = []
    for t in range(testcase):
        b = deepcopy(board)
        for dir in rule[t]:
            rotate_1(dir,b)
            rotate_2(dir, b)
            # print(b[1])
        answer.append(b[1])
    
    idx = 0
    for i in answer:
        for k in range(3):
            for j in range(3):
                print(i[idx],end="")
                idx += 1
            print()
        idx = 0

testcase = int(input())
rule = []
for i in range(testcase):
    n = int(input())
    rule.append(list(map(str,input().split())))

solution(testcase, rule)