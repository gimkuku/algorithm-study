def solution(n, k, board):
    # 물고기가 가장 적은 어항에 한마리씩
    min_fish = float('inf')
    max_fish = -1
    for idx in range(n):
        if min_fish > board[0][idx]: min_fish = board[0][idx]
        if board[0][idx] > max_fish: max_fish = board[0][idx]
    if max_fish - min_fish <= k:
        print(0)
        return

    flag = True
    answer = 1
    while flag:
        for idx in range(n):
            if min_fish == board[0][idx]:
                board[0][idx] += 1
            
        # 어항 쌓기
        height = 1
        start = 0
        length = 1
        # print(board)
        while (n - start - length) >= height:
            # width에서 length 만큼 블록 공중 부양
            idx = 1+length
            for i in range(start,start+length):
                idx -= 1
                # 어항 옮기기
                for j in range(height):
                    board[idx][start+length+j] = board[j][i]
            # 어항 옮기면 0 넣어주기
            for i in range(start,start+length):
                for j in range(n):
                    board[j][i] = 0
            start = start + length
            prev_height = height
            height = 1 + length
            length = prev_height

            # # #############
            # for i in range(n):
            #     print(board[i])
            # print("\n")
            # # #############
        
        # 물고기 수 조절
        # diff : [큰세,큰가,작세,작가,차이]
        diff = []
        for i in range(0, height):
            for j in range(start, n):
                # 아래랑 비교
                if (board[i + 1][j] != 0):
                    if board[i + 1][j] > board[i][j]:
                        d = board[i + 1][j] - board[i][j]
                        if d >= 5: diff.append([i + 1, j, i, j, d // 5])
                    else:
                        d = board[i][j] - board[i + 1][j]
                        if d >= 5: diff.append([i, j, i + 1, j, d // 5])
                # 왼쪽이랑 비교
                if (j+1 < n) and (board[i][j+1] != 0):
                    if board[i][j + 1] > board[i][j]:
                        d = board[i][j+1] - board[i][j]
                        if d >= 5: diff.append([i, j+1, i, j, d // 5])
                    else:
                        d = board[i][j] - board[i][j+1]
                        if d >= 5: diff.append([i, j, i, j + 1, d // 5])
                        
        for bigy, bigx, smally, smallx, d in diff:
            board[bigy][bigx] -= d
            board[smally][smallx] += d
        
        # #############
        # print("굴린 다음에 분배")
        # for i in range(n):
        #     print(board[i])
        # print("\n")
        # # #############

        # 다시 일열로 놓기
        idx = 0
        for i in range(start, n):
            for j in range(length + 1):
                if board[j][i] == 0:
                    break
                else:
                    board[0][idx] = board[j][i]
                    idx += 1
                    if j!= 0:
                        board[j][i] = 0

        # # #############
        # print("굴린뒤 결과")
        # print(board[0])
        # print("\n")
        # print("반쪼개서 위로 올리기")
        # ############

        # 반쪼갠거 거꾸로 올리기
        for i in range(0,n // 2):
            board[1][n-i-1] = board[0][i]
            board[0][i] = 0
        #############
        # for i in range(n):
        #     print(board[i])
        # print("\n")
        # #############
        # 한번 더 반쪼개서 위로 올리기
        for i in range(0,n // 4):
            for j in range(2):
                board[3-j][n-i-1] = board[j][i + n // 2]
                board[j][i+n // 2] = 0
        

        # 물고기 수 조절
        diff = []
        for i in range(4):
            for j in range(n - n // 4, n):
                # 아래랑 비교
                if (i + 1 < n):
                    if (board[i + 1][j] != 0):
                        if board[i + 1][j] > board[i][j]:
                            d = board[i + 1][j] - board[i][j]
                            if d >= 5: diff.append([i + 1, j, i, j, d // 5])
                        else:
                            d = board[i][j] - board[i + 1][j]
                            if d >= 5: diff.append([i, j, i + 1, j, d // 5])
                # 왼쪽이랑 비교
                if (j + 1 < n):
                    if (board[i][j+1] != 0):
                        if board[i][j + 1] > board[i][j]:
                            d = board[i][j+1] - board[i][j]
                            if d >= 5: diff.append([i, j+1, i, j, d // 5])
                        else:
                            d = board[i][j] - board[i][j+1]
                            if d >= 5: diff.append([i, j, i, j + 1, d // 5])
                        
        for bigy, bigx, smally, smallx, d in diff:
            board[bigy][bigx] -= d
            board[smally][smallx] += d
        
        # #############
        # print("반 쪼개서 두번하고 분배")
        # for i in range(n):
        #     print(board[i])
        # print("\n")
        #############
        
        # 제일 많은것과 제일 작은것 차이
        min_fish = float('inf')
        max_fish = -1

        # 다시 일열로 놓기
        idx = 0
        for i in range(n - n // 4, n):
            for j in range(4):
                # print(board[j][i])
                if board[j][i] == 0: break
                if board[j][i] > max_fish: max_fish = board[j][i]
                if board[j][i] < min_fish: min_fish = board[j][i]
                board[0][idx] = board[j][i]
                idx += 1
                if j!= 0:
                    board[j][i] = 0
                
        
        # ###########
        # print("사이클 한번 끝")
        # print(board[0])
        # #############

        if max_fish - min_fish <= k:
            break
        else: answer += 1
    print(answer)

n, k = map(int, input().split())
# 이중배열. 첫번째 인덱스가 높이
board = []
board.append(list(map(int, input().split())))
for i in range(n - 1):
    board.append([0 for i in range(n)])
solution(n,k,board)