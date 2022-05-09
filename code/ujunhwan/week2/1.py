def dfs(x, visited, available, sheep, wolf):
    global ans
    
    if sheep <= wolf:
    	return 
    
    visited[x] = 1
    
    available.discard(x)
    
    for y in adj[x]:
        if visited[y] == 0:
            available.add(y)
    
    ans = max(ans, sheep)
    
    for y in available:
        if info[y] == 1:
            dfs(y, visited[:], available.copy(), sheep, wolf+1)
        else:
            dfs(y, visited[:], available.copy(), sheep+1, wolf)

def solution(arr, edges):
    global info, adj, ans
    info = arr
    ans = 0
   	 
    adj = [[] for col in range(17)]
    
    for parent, child in edges:
        adj[parent].append(child)
    
    visited = [0] * 17
    available = set([])
    dfs(0, visited.copy(), available.copy(), 1, 0)
        
    return ans