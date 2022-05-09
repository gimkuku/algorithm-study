def decimal_to_k(n, k):
    to_k = ""
    div = n
    while (div > 0):
      to_k += str(div % k)
      div = div // k
    return to_k[::-1]

def is_prime(n):
    if (n == 1): return False
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0): return False
    return True

def count_prime(n):
    count = 0
    for i in n.split('0'):
        if i != "":
            if is_prime(int(i)):
                count += 1
    return count
    
def solution(n, k):
    to_k = decimal_to_k(n,k)
    return count_prime(to_k)
  
