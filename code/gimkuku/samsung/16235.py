def solution(n, m, k, add, trees):
    board = [[5 for _ in range(n)] for _ in range(n)]
    dirs = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
    cnt = m
    for i in trees:
        trees[i].sort()
    # print(trees)
    
    for year in range(k):
        # 봄
        # 나이 어린 순으로 나무 sort
        death_pos = []
        death = []
        for tree in trees:
            x,y = map(int, tree.split('_'))
            for idx,element in enumerate(trees[tree]):
                if board[x - 1][y - 1] >= element:
                    board[x - 1][y - 1] -= element
                    trees[tree][idx] = element+1 
                else:
                    death.append([x,y,idx])
                    break
        # 여름
        for tree in death:
            x, y, idx = tree
            key = ''+str(x)+'_'+str(y)
            for age in trees[key][idx:]:
                cnt -= 1
                board[x - 1][y - 1] += age // 2
            trees[key] = trees[key][:idx]
        
        # 가을
        # print(trees)
        for tree in trees.copy():
            x, y = map(int, tree.split('_'))
            # print(trees[tree])
            for age in trees[tree]:
                # print("age",age)
                # 5의 배수이면
                if age % 5 == 0:
                    for dx, dy in dirs:
                        if x + dx - 1 < 0 or x + dx - 1 > n - 1 or y + dy - 1 < 0 or y + dy - 1 > n - 1: continue
                        key = '' + str(x + dx) + '_' + str(y + dy)
                        if key in trees:
                            trees[key].insert(0, 1)
                        else:
                            trees[key] = [1]
                        cnt += 1
        # 겨울
        for i in range(n):
            for j in range(n):
                board[i][j] += add[i][j]

    print(cnt)

n, m, k = map(int, input().split())
add = []
trees = {}
for i in range(n):
    add.append(list(map(int, input().split())))
for i in range(m):
    x, y, age = map(int, input().split())
    str_key = '' + str(x) + '_' + str(y)
    if str_key in trees:
        trees[str_key].append(age)
    else:
        trees[str_key] = [age]
    
solution(n,m,k,add,trees)