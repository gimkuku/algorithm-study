from collections import deque

def bfs(n, apeachInfo):
    maxGap = 0
    deq = deque([(0, [0 for i in range(len(apeachInfo))])])
    res = []
    while deq:
        cnt, ryanInfo = deq.popleft()
        
        if sum(ryanInfo) == n:
            apeachSum, ryanSum = 0, 0
            for i in range(len(apeachInfo)):
                if not (apeachInfo[i] == 0 and ryanInfo[i] == 0):
                    if apeachInfo[i] >= ryanInfo[i]:
                        apeachSum += 10 - i
                    else:
                        ryanSum += 10 - i
            if apeachSum < ryanSum:
                gap = ryanSum - apeachSum
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                res.append(ryanInfo)
                
        elif sum(ryanInfo) > n:
            continue
        
        elif cnt == 10:
            tmp = ryanInfo.copy()
            tmp[cnt] = n - sum(tmp)
            deq.append((cnt+1, tmp))
        
        else:
            more = ryanInfo.copy()
            more[cnt] = apeachInfo[cnt]+1 
            deq.append((cnt+1, more))
            zero = ryanInfo.copy()
            zero[cnt] = 0
            deq.append((cnt+1, zero))
    
    return res

def solution(n, info):
    result = bfs(n, info)
    if not result:
        return [-1]
    elif len(result) == 1:
        return result[0]
    else:
        return result[-1]
