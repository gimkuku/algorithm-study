def solution(n, s, a, b, fares):
    answer = float('inf')
    
    adj = [[float('inf') for col in range(201)] for row in range(201)]
    
    for c, d, f in fares:
        adj[c][d] = min(adj[c][d], f)
        adj[d][c] = min(adj[d][c], f)
    
    for i in range(1, n+1):
        adj[i][i] = 0
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
   	
    print(s, a, b)
    
    for mid in range(1, n+1):
        answer = min(answer, adj[mid][a] + adj[mid][b] + adj[mid][s])
        
    return answer