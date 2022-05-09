import re


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return sieve


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def radix_convert(num, radix):
    answer = ""
    target = num

    while target != 0:
        remainder = target % radix
        answer = str(remainder) + answer

        target //= radix

    return answer


def solution(n, k):
    answer = 0
    sieve = prime_list(1000001)
    sieve[0] = sieve[1] = False

    radix_converted_number = radix_convert(n, k)
    splited_number = re.split("0+", radix_converted_number)

    for num in splited_number:
        if num == "":
            continue

        try:
            if sieve[int(num)]:
                answer += 1
        except IndexError:
            if is_prime(int(num)):
                answer += 1

    return answer
