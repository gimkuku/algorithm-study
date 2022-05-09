import math
def is_prime(n):
    if n < 2:
        return False

    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def decimal_to_k_notation_converter(n,k):
    tmp = ''
    while n > 0:
        tmp += str(n%k)
        n //= k
    return tmp[::-1]

def solution(n, k):
    answer = 0
    converted_n = decimal_to_k_notation_converter(n,k)
    numbers = converted_n.split('0')
    
    for number in numbers:
        if number == '':
            continue
        if is_prime(int(number)):
            answer += 1
    return answer