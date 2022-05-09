# WIL : Week 1
1주차에 대한 WIL
## 소수 구하기
- n이 소수인지 확인하기 위해 2~루트n 까지 나눠보며 확인할 수 있다. n의 약수가 대칭적이기 때문이다. O(루트n)
- 에라토스테네스의 체 알고리즘을 통해 1~n까지의 수 중 소수를 구할 수 있다.
## 리스트 뒤집기
```python
a = '12345'
print(a[::-1])
> '54321'
```
## 10진법->k진법 변환
- k로 몫이 0일때까지 계속 나누며 나머지를 구한다
- 구한 나머지들의 순서를 뒤집는다
## sorted 내장 함수로 Dictionary 정렬
```python
d = dict()
d['a'] = 66
d['i'] = 20
d['e'] = 30
d['d'] = 33
d['f'] = 50
d['g'] = 60
d['c'] = 22
d['h'] = 80
d['b'] = 11
 
# 1. 딕셔너리 출력
print("\n1. 기본 딕셔너리")
print(d)
 
# 딕셔너리 키 정렬 오름차순(디폴트)
print("\n2. 키 정렬 sorted(d.items())")
f = sorted(d.items())
print(f)
 
# 딕셔너리 키 정렬 내림차순
print("\n3. 키 정렬 sorted(d.items(), reverse=True)")
g = sorted(d.items(), reverse=True)
print(g)
 
# 딕셔너리 키만 정렬 및 출력1
print("\n4. 키만 정렬 sorted(d.keys())")
h = sorted(d.keys())
print(h)
 
# 딕셔너리 키만 정렬 및 출력2
print("\n5. 키만 정렬 sorted(d)")
i = sorted(d)
print(i)
```
출력 결과
```
1. 기본 딕셔너리
{'a': 66, 'i': 20, 'e': 30, 'd': 33, 'f': 50, 'g': 60, 'c': 22, 'h': 80, 'b': 11}

2. 키 정렬 sorted(d.items())
[('a', 66), ('b', 11), ('c', 22), ('d', 33), ('e', 30), ('f', 50), ('g', 60), ('h', 80), ('i', 20)]

3. 키 정렬 sorted(d.items(), reverse=True)
[('i', 20), ('h', 80), ('g', 60), ('f', 50), ('e', 30), ('d', 33), ('c', 22), ('b', 11), ('a', 66)]

4. 키만 정렬 sorted(d.keys())
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

5. 키만 정렬 sorted(d)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
```
### Ref
[파이썬 정렬 sorted 함수 정리 및 예제](https://blockdmask.tistory.com/466)
## itertools 라이브러리
```python
from itertools import permutations, product, combinations, combinations_with_replacement

s = 'ABC'

a = [x for x in permutations(s, 2)]
print(a)
#[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

b = [x for x in product(s, repeat=2)]
print(b)
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

c = [x for x in combinations(s,2)]
print(c)
#[('A', 'B'), ('A', 'C'), ('B', 'C')]

d = [x for x in combinations_with_replacement(s,2)]
print(d)
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```
# kakao_92335 : K진수에서 소수 개수 구하기
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92335
## Unsolved Code
```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2,n):
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
```
### 결과
테스트 16개 중 1개 시간초과로 실패
### 접근
1. string으로 n을 10진법 -> k진법으로 변환한다.
2. 변환된 수(string)을 '0'으로 구분(split)한다. 이렇게 하면 문제에서 나온 '0P0', 'P0', '0P', 'P' 네가지 경우의 수를 추출할 수 있다.
3. 순회하며 소수인지 아닌지 판별한다. 이 때 구분된 리스트(numbers)에 ''이 있으면 continue로 예외처리.
### 회고
소수 판별 과정이 너무 naive해서 시간초과가 뜨는 것 같다. 방법론을 조금 더 알아보고 시도해야겠다.

## Solved Code
```python
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
```
### 결과
성공
### 접근
위와 동일하나 소수 판별에 차이가 있다. n을 2부터 n까지 나눠보며 소수를 판별하는 것이 아닌, 2부터 루트n 까지 나눠보며 판별한다.

위의 방법이 유효한 이유를 16을 예시로 설명하겠다. 16은 1, 2, 4, 8, 16 이 약수다. 이 때 16 = 1 * 16 = 2 * 8 = 4 * 4 라는 대칭 구조를 띈다. 따라서 1 ~ 16까지 나눠보며 소수인지 아닌지 판별 할 필요 없이 16의 제곱근인 4 까지만 나눠봐도 이를 판별할 수 있다 :)

## 92335번 문제 회고
학교에서 c언어만 하다가 다시 파이썬 코테로 넘어오니 엄청 버벅거렸다,,,ㅠㅠ. 문제를 처음 봤을 때 몇가지 스텝으로 문제를 쪼갤 수 있었다. 하지만 거기까지고 구현하려고 하니 막혔다. 진법 변환부터 막혀서 다시 구글링 해보고 유튜브로 파이썬 문법 강의도 다시 듣고 문제로 돌아왔다. 

그렇게 첫 번째 코드를 완성했지만 시간초과가 떴다. 조건에 1 ≤ n ≤ 1,000,000에 정확성 테스트 10초(?)라 나와있어서 시간초과가 안 뜰줄 알았는데 실행시간 계산을 어떻게 하는거지..? 어쨋든 나동빈좌의 소수 판별 알고리즘 기법을 통해 O(n) -> O(루트n) 으로 개선하여 문제를 풀 수 있었다.

그리고 강의를 보며 <strong>에라토스테네스의 체</strong> 라는 알고리즘도 처음 알게 되었는데, 이는 어떤 범위 안의 수들이 소수인지 판별할 때 쓰인다고 한다. 이번 문제에서는 범위가 주어졌다고 생각하지 않아 이 알고리즘을 적용하지 않았다.

## Ref
[나동빈의 이코테 강의 : 소수 판별 알고리즘](
https://www.youtube.com/watch?v=CyINCmJPjfM&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=37)

# kakao_92341 : 주차 요금 계산
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92341
## Solved Code
```python
def calc_fee(table, fees):
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    
    answer = []
    for info in table:
        time = info[1]['time']
        if time <= default_time:
            answer.append(default_fee)
        else:
            if (time - default_time) % unit_time != 0:
                time = (time - default_time) // unit_time + 1
            else:
                time = (time - default_time) // unit_time
            answer.append(default_fee + time * unit_fee)
    return answer

def convert_to_minute(hhmm):
    splited_hhmm = hhmm.split(":")
    hour = splited_hhmm[0]
    minute = splited_hhmm[1]
    return int(hour)*60 + int(minute)

def solution(fees, records):
    answer = []
    table = dict()
    end_time = convert_to_minute("23:59")
    for record in records:
        # 데이터 추출
        data = record.split(" ")
        time = convert_to_minute(data[0])
        car_number = data[1]
        is_in = True if data[2] == "IN" else False
        
        # 입차 / 출차 여부 확인
        if is_in:
            # 처음 입차한 경우
            if car_number not in table:
                info = dict()
                info['in_time'] = time # 입차 시각(분)
                info['is_in'] = is_in # 현재 입차 여부
                info['time'] = 0 # 누적 시간
                table[car_number] = info
            # 두 번 이상 입차한 경우
            else:
                table[car_number]['in_time'] = time
                table[car_number]['is_in'] = is_in
        else:
            table[car_number]['is_in'] = is_in
            table[car_number]['time'] += time - table[car_number]['in_time']
            pass
        
    # 23:59까지 입차한 차량 확인 후 시간 계산
    for car_number in table:
        if table[car_number]['is_in']:
            table[car_number]['time'] += end_time - table[car_number]['in_time']
    
    # 차량 번호대로 정렬된 튜플 배열 생성
    sorted_tuple_table = sorted(table.items())
    
    # 주차 요금 계산
    answer = calc_fee(sorted_tuple_table, fees)
        
    return answer
```
### 결과
성공
### 접근
- 스트링 데이터를 차례로 읽어 " "으로 split 하여 변수에 나눠 담는다.
- 이 때, 입차/출차 시각은 `convert_to_minute` 메소드를 통해 분으로 저장하며, `is_in`에 입차/출차에 따라 True/False를 담는다.
- `is_in`으로 입차/출차 분기 처리를 하며, 입차시에도 첫 입차인지 두번째 이상의 입차인지 분기처리 한다.
- 데이터는 `table`이라는 Dictionary에 다음과 같은 형태로 저장한다.
```python
{
  "5123": {          # 차량 번호
    "in_time" : 360, # 최근 입차 시각 (분)
    "is_in" : True,  # 현재 입차했는지 여부
    "time" : 0,      # 누적 시간 계산
  },
  ...
}
```
- 출차시에 출차시각과 최근 입차시각의 차를 누적 시간에 저장한다.
- 23:59까지 출차하지 않은 차량을 확인하여 누적 시간을 갱신한다.
- `sorted(table.items())`을 통해 차량번호에 대해 정렬한다. 튜플 배열이 리턴된다.
- 정렬된 튜플배열로 금액을 계산하여 정답을 구한다.

## 92341번 문제 회고
쉬울 줄 알았는데 낑낑대며 더럽게 풀었다...ㅠㅠ 빠르고 효율적이게 구현하는 능력을 길러야겠다...

문제를 풀 때부터 `데이터의 저장 방식`, 동시에 `정렬 방법`에 대해 고민하며 접근했다. 많은 정보를 담기 위해 개발하며 다룬 DB와 유사한 key-value 로직의 Dictionary를 이용했다. 또한 정렬시에는
`sorted(table.items())`을 통해 Dictionary를 정렬했다(구글링함).

# kakao_92342 : 양궁 대회
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92342
## Unsolved Code
```python
from itertools import product, combinations

def get_all_combinations(n):
    comb = []
    # n을 1~n개로 쪼개는 모든 경우를 순회
    for k in range(1,n+1):
        # n을 k개로 쪼개는 모든 중복순열 중 합이 n인 것
        products = [x for x in product(range(1,n+1), repeat = k) if sum(x) == n]
        # 0~10 중 k개의 인덱스를 고른 튜플 리스트
        indices_list = [x for x in combinations(range(11), k)]
        for prod in products:
            for indices in indices_list:
                tmp = [0]*11
                # 인덱스 튜플을 순회하며 tmp 인덱스 값 을 대응하는 중복순열 값으로 대치
                for i, index in enumerate(indices):
                    tmp[index] = prod[i]
                comb.append(tmp)
    return comb

def calc_score_difference(apeach, lion):
    apeach_score, lion_score = 0, 0
    for i in range(11):
        if apeach[i] < lion[i]:
            lion_score += 10-i
        elif apeach[i] == 0 and lion[i] == 0:
            continue
        else:
            apeach_score += 10-i
    return lion_score - apeach_score

def compare_and_get_answer(a,b):
    # 어피치와 같은 점수차를 낼 수 있는 두 list a, b 중
    # 낮은 점수를 더 많이 맞힌 경우를 찾아서 return
    for i in reversed(range(11)):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            return a
        else:
            return b

def solution(n, info):
    answer = []
    max_d_score = -99999 # 점수차 초기화
    for lion_info in get_all_combinations(n):
        d_score = calc_score_difference(info, lion_info) # 점수차 계산
        if d_score == max_d_score: # 지금까지의 최대점수차와 같은 경우
            answer = compare_and_get_answer(answer, lion_info) # 조건에 맞는 값 구하기
        elif d_score > max_d_score: # 최대점수차 갱신
            max_d_score = d_score
            answer = lion_info
        else:
            continue

    if max_d_score <= 0: # 최대점수차가 0 이하라면 비기거나 지는 경우
        answer = [-1]
    return answer
```
### 결과
테스트 케이스 4개 중 2개 시간초과로 실패
### 접근
- 어피치와 라이언의 최대 점수차인 `max_d_score`를 -99999로 초기화한다.
- `get_all_combinations` 메소드로 라이언이 만들 수 있는 모든 점수 조합 리스트를 구한다.
- n을 k개(1~n)로 쪼갤 수 있는 모든 경우의 수에 대해 -> 10~0 중 k개의 인덱스를 고른 뒤 -> 대응되는 인덱스에 k개로 쪼갠 수들을 넣어주는 방식으로 위의 함수를 구현한다.
- `get_all_combinations`에서 리턴한 리스트를 순회하며 점수차를 계산한다.
- 점수차가 `max_d_score`보다 크면 `max_d_score`와 answer을 갱신한다.
- 점수차가 `max_d_score`와 같다면, `가장 낮은 점수를 더 많이 맞힌 경우`의 조건을 만족하는 답을 구하기 위해 `compare_and_get_answer`로 비교 후 answer을 갱신하거나 그대로 둔다.
- 마지막으로 최대 점수차가 0 이하라면 비기거나 지는 경우이므로 [-1]을 리턴한다. 
### 회고
라이언이 만들어낼 수 있는 모든 점수의 조합을 찾는 코드를 구현하는데 너무너무 어려웠다. 라이언이 승리할 수 있는 조건이 까다롭게 느껴져 모든 경우의 수를 구한 뒤 하나씩 검사하는 과정을 따라가보려 했다. 결국 라이언의 점수 조합을 모두 찾는 `get_all_combinations` 메소드를 만들며 엄청 오랜 시간을 썼고 또 더럽게 코딩했다(4중 포문;;).

테스트 케이스 2개는 통과했으나 2개는 시간초과가 떴다. 시간초과가 뜰 각오는 하고 있었지만 이렇게라도 구현해보고싶었다. 이제 다른 방법을 찾아봐야겠다

## Solved Code
```python
#from itertools import product, combinations
from itertools import combinations_with_replacement

'''
def get_all_combinations(n):
    comb = []
    # n을 1~n개로 쪼개는 모든 경우를 순회
    for k in range(1,n+1):
        # n을 k개로 쪼개는 모든 순열
        products = [x for x in product(range(1,n+1), repeat = k) if sum(x) == n]
        # 0~10 중 k개의 인덱스 선택
        indices_list = [x for x in combinations(range(11), k)]
        for prod in products:
            for indices in indices_list:
                tmp = [0]*11
                for i, index in enumerate(indices):
                    tmp[index] = prod[i]
                comb.append(tmp)
    return comb
'''
def get_all_combinations(n):
    comb = []
    for indices in combinations_with_replacement(range(11), n):
        tmp = [0]*11
        for index in indices:
            tmp[index] += 1
        comb.append(tmp)
    return comb

def calc_score_difference(apeach, lion):
    apeach_score, lion_score = 0, 0
    for i in range(11):
        if apeach[i] < lion[i]:
            lion_score += 10-i
        elif apeach[i] == 0 and lion[i] == 0:
            continue
        else:
            apeach_score += 10-i
    return lion_score - apeach_score

def compare_and_get_answer(a,b):
    # 어피치와 같은 점수차를 낼 수 있는 두 list a, b 중
    # 낮은 점수를 더 많이 맞힌 경우를 찾아서 return
    for i in reversed(range(11)):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            return a
        else:
            return b

def solution(n, info):
    answer = []
    max_d_score = -99999 # 점수차 초기화
    for lion_info in get_all_combinations(n):
        d_score = calc_score_difference(info, lion_info)
        if d_score == max_d_score:
            answer = compare_and_get_answer(answer, lion_info)
        elif d_score > max_d_score:
            max_d_score = d_score
            answer = lion_info
        else:
            continue

    if max_d_score <= 0:
        answer = [-1]
    return answer
```
### 결과
성공
### 접근
위의 방식과 접근은 동일하나 `combinations_with_replacement` 함수를 개선했다.
```python
from itertools import combinations_with_replacement
combinations_with_replacement(range(11), n):
```
위의 함수 호출을 통해 0~11을 중복으로 n개 뽑을 수 있는 모든 조합을 알려준다.
예를 들어 n이 3이라면 (3,3,5), (10,10,10)이 있을 수 있다. (3,3,5)의 의미는 3점을 2번, 5점을 1번 맞춘 것이며, (10,10,10)의 의미는 10점을 3번 맞춘 것이다.

요구하는 answer의 형태로 표현하면 (10,10,10)의 경우 [3,0,0,0,0,0,0,0,0,0,0]이 될 것이다.

이 과정은 시간초과가 발생하지 않는 이유는 `nH11`의 최대값은 `10H11` = `20C10`으로 대략 18만 가지의 경우의수밖에 되지 않기 때문이다.
## 92342번 문제 회고
분명 중복조합인데 바보같이 너무 어렵게 중복조합 문제를 풀려고 하다보니 불필요한 계산량 증가로
시간초과로 이어진 것 같다. 중복조합 수학문제를 풀 때 `칸막이를 두고 나열하는 문제`로 변환하여 풀던 습관때문에 시야가 좁았다.

`itertools` 라이브러리는 수학과 관련된 강력한 기능들을 제공한다. product, combinations, combinations_with_replacement 같은 메소드를 적절히 사용할 수 있도록 많이 적용해봐야 할 듯 하다.