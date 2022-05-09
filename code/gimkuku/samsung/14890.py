def solution(n, l, board):
    answer = 0
    for i in range(n):
        temp = board[i][0]
        cnt = 1
        flag = True
        slope = [0,0]
        for j in range(1, n):
            if max(temp, board[i][j]) - min(temp, board[i][j]) > 1:
                flag = False
                break
            if slope[0] > 0:
                if board[i][j] == slope[1]:
                    slope[0] = slope[0] - 1
                    temp = board[i][j]
                    # print(cnt)
                    continue
                else:
                    slope = [0, 0]
                    flag = False
                    break
            # 다음게 더 높으면
            if board[i][j] > temp:
                # print(cnt, l)
                if cnt < l:
                    flag = False
                    break
                cnt = 1
            # 같으면 cnt ++ 
            elif board[i][j] == temp:
                cnt += 1
            # 다음게 낮으면
            elif board[i][j] < temp:
                cnt = 0
                slope = [l -1, board[i][j]]
            temp = board[i][j]
        if flag and slope[0] == 0:
            # print(board[i])
            answer += 1
        
    for i in range(n):
        temp = board[0][i]
        cnt = 1
        flag = True
        slope = [0,0]
        for j in range(1, n):
            if max(temp, board[j][i]) - min(temp, board[j][i]) > 1:
                flag = False
                break
            # 경사로 만드는 중
            if slope[0] > 0:
                if board[j][i] == slope[1]:
                    slope[0] = slope[0] - 1
                    temp = board[j][i]
                    # print(cnt)
                    continue
                else:
                    slope = [0, 0]
                    flag = False
                    break
            # 다음게 더 높으면
            if board[j][i] > temp:
                # 경사로 못만들면 끝
                if cnt < l:
                    flag = False
                    break
                # 경사로 만들었으면 다음것부터 타일 연속 개수 세기
                cnt = 1
            # 같으면 cnt ++ 
            elif board[j][i] == temp:
                cnt += 1
            # 다음게 낮으면
            elif board[j][i] < temp:
                cnt = 0
                # 경사로 만들기 시작
                slope = [l -1, board[j][i]]
            temp = board[j][i]
        if flag and slope[0] == 0:
            # for j in range(n):
            #     print(board[j][i], end="")
            # print("\n")
            answer += 1
    print(answer)
    return answer


n, l = map(int,input().split())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))
solution(n,l,board)