def getNextNodes(edges, node):
    nextNodes = []
    
    for e in edges:
        i,j = e
        if node == i:
            nextNodes.append(j)
            
    return nextNodes
    
def dfs(info, edges, sheep, wolf, cnt, path):
    if info[cnt]:
        wolf += 1
    else:
        sheep += 1
        
    if sheep <= wolf:
        return 0
    
    maxSheep = sheep
    
    for p in path:
        for n in getNextNodes(edges, p):
            if n not in path:
                path.append(n)
                maxSheep = max(maxSheep, dfs(info, edges, sheep, wolf, n, path))
                path.pop()
                
    return maxSheep
        
def solution(info, edges):
    sheep = 0
    wolf = 0
    cnt = 0
    path = [0]
    answer = dfs(info, edges, sheep, wolf, cnt, path)
    
    return answer
