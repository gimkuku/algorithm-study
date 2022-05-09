# k진수에서 소수 개수 구하기

def convert(n, k):
    if n < k:
        return str(n)
    
    ret = ''
    
    while n >= k:
        [n, mod] = divmod(n, k)
        ret = str(mod) + ret
    
    if n > 0:
        ret = str(n) + ret
        
    return ret

def sieve(n):
    isPrime[0] = False
    isPrime[1] = False

    maxNumber = (n ** 0.5) + 1
    
    for i in range(2, maxNumber):
        if isPrime[i]:
            for j in range(i+i, maxNumber, i):
                isPrime[j] = False


def solution(n, k):
    answer = 0
    numStr = convert(n, k).split('0')

    global isPrime
    isPrime = [True] * (n+1)

    sieve(n)
    
    for number in numStr:
        if len(number) < 1:
            continue
            
        if isPrime[int(number)] is True:
            answer += 1
            
    return answer