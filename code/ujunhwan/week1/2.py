def calc(ryan):
    global apeach
    a = r = 0
    for i in range(10):
        if (apeach[i] == 0) and (ryan[i] == 0):
            continue

        if apeach[i] >= ryan[i]:
            a += (10-i)
        else: r += (10-i)

    return r - a


def dfs(idx, left, ryan):
    global answer, max_score
    if left > 0 and idx == -1:
        return
    
    if left == 0:
        cand_value = calc(ryan)
        if cand_value > max_score:
            answer = ryan[:]
            max_score = cand_value
        return
        
    for i in range(left, -1, -1):
        ryan[idx] += i 
        dfs(idx-1, left-i, ryan[:])
        ryan[idx] -= i
        

def solution(n, info):
    global answer, max_score, apeach
    apeach = info
    answer = [0 for col in range(10+1)]
    max_score = -100000
    
    dfs(10, n, [0 for col in range(10+1)])
        
    print(max_score)
    return [-1] if max_score <= 0 else answer