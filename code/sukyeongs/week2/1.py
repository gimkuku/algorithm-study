def solution(info, edges):
    
    def nextNodes(v):
        temp = list()
        for e in edges:
            i, j = e 
            if v == i:
                temp.append(j)
        return temp
    
    def dfs(sheep, wolf, current, path): 
        
        if info[current]:
            wolf += 1
        else:
            sheep += 1 
            
        if sheep <= wolf:
            return 0 
        
        maxSheep = sheep 
        
        for p in path: 
            for n in nextNodes(p): 
                if n not in path: 
                    path.append(n) 
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n, path))
                    path.pop() 
                    
        return maxSheep
    
    answer = dfs(0, 0, 0, [0])
    
    return answer
