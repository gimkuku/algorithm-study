def solution(enroll, referral, seller, amount):
    # referral[i] = enroll[i]'s parent
    # referral[i] = "-" : root
    
    size = len(enroll)
    
    money = [0 for col in range(size)]
    adj = [-1 for col in range(size)]
    
    dic = {}
    
    dic['-'] = -1
    
    def dfs(x, add):
        if x == -1 or add == 0:
            return
        
        money[x] += add - add // 10
        dfs(adj[x], add // 10)
    
    for i in range(size):
        dic[enroll[i]] = i
    
    for i in range(size):
        parent = int(dic[referral[i]])
        child = int(dic[enroll[i]])
        adj[child] = parent
            
    for i in range(len(seller)):
        if amount[i] == 0:
            continue
        index = int(dic[seller[i]])
        dfs(index, amount[i]*100)
        
    return money