def solution(n, k):
    rev_base=''
    
    while n:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    
    rev_base = rev_base[::-1]
    
    lis = rev_base.split('0')
    result = []
    for i in lis:
        if len(i)>0:
            result.append(i)
    lis = list(map(int,result))
    
    count=0
    for i in lis:
        prime = True
        if i < 2 :
            continue
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                prime = False
                break
        if prime:
            count+=1
    return count
