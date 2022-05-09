import bisect as bs

def solution(n, weak, dist):
    wsize = len(weak)
    dsize = len(dist)
    
    w_visited = [False for _ in range(2*wsize)]
    d_visited = [False for _ in range(dsize)]
    
    for i in range(wsize):
        weak.append(weak[i]+n)
    
    print(weak)
    def dfs(sidx, widx, left):
        # start is weak point value
        ret = float('inf')
        
        if weak[widx] > weak[sidx+wsize-1]:
            #print(f"{weak[sidx]} START // {weak[widx]} END ?? {weak[sidx+wsize-1]}")
            return 0
        
        if left == 0:
            return float('inf')
        
        for i in range(dsize):
            # upper bound
            next_widx = bs.bisect_right(weak, weak[widx]+dist[i])
            
            if next_widx == len(weak):
                return 1
                
            #print(f"cur value : {weak[widx]} + {dist[i]} next value : {weak[next_widx]} ")
            if not w_visited[next_widx] and not d_visited[i]:
                w_visited[next_widx] = True
                d_visited[i] = True
                ret = min(ret, dfs(sidx, next_widx, left-1) + 1)
                w_visited[next_widx] = False
                d_visited[i] = False
                
        return ret
        
    ans = float('inf')
    
    # start everywhere
    for i in range(wsize):
        w_visited[i] = True
        ans = min(ans, dfs(i, i, dsize))
        w_visited[i] = False
        
    if ans == float('inf'):
        return -1
    return ans