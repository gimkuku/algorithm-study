# Week 1

## 1. k진수에서 소수 개수 구하기
```python
# 양의 정수 n을 k진수로 바꾸는 함수 (리턴값 : 양의 정수 n을 k진수로 바꾼 문자열)
def decimal_to_k(n, k):
  
    # to_k :n을 k진수로 바꾼 문자열
    # n을 k로 나누었을 때 나머지값들이 순서대로 저장된다. 
    # 더 이상 나누어지지 않을 때, 문자열을 뒤집어 리턴한다.
    
    # div : n을 k로 나누었을 때 몫
    # 이 값이 0보다 클 때 까지 나머지를 구해 나머지값을 to_k에 이어 저장한다.
    
    to_k = ""
    div = n
    
    while (div > 0):
        to_k += str(div % k)
        div = div // k
        
    return to_k[::-1]


  
# 소수 판별 함수 (리턴값 : 정수 n이 소수이면 True, 소수가 아니면 False)
def is_prime(n):
  
    # 처음에 2부터 n까지 반복하며 나머지가 0일 경우 False를 리턴했는데,
    # n이 매우 큰 경우인 테케 1에서 시간 초과가 났다. (제한사항 : 1 ≤ n ≤ 1,000,000)
    # n의 약수는 n의 제곱근을 중심으로 대칭적으로 나타나기 때문에
    # 2부터 n의 제곱근까지로 반복 길이 조정
    
    if (n == 1): return False
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0): return False
    return True

  
  
# 소수 개수 구하는 함수 (리턴값 : 문자열 n을 0으로 분할했을 때, 나타나는 소수의 개수)
def count_prime(n):
  
    # count : 문자열 n을 검사했을 때, 소수가 나타나는 횟수
    # 문자열 n을 0으로 분할하고 분할된 문자열이 소수인 경우 count 증가
    
    count = 0
    for i in n.split('0'):
        if i != "":
            if is_prime(int(i)):
                count += 1
    return count
    
    
    
def solution(n, k):
    to_k = decimal_to_k(n,k)
    return count_prime(to_k)
```

## 2. 양궁 대회
```python
# 깊이 탐색을 통해 나온 (현재 순서, 현재 라이언의 점수 별 화살 개수 배열)들을 저장하고 다시 반복하기 위해 deque 도입 
from collections import deque

# 깊이 탐색 (리턴값 : "라이언이 가장 큰 점수 차이로 우승하기 위한 10점부터 0점까지 맞춘 화살 개수 배열"들의 배열)
def bfs(n, apeachInfo):
  
    # n : 주어진 화살의 개수
    # apeachInfo : 어피치의 점수 별 화살 개수 배열
    
    # maxGap : 최대 점수 차 
    # = 0으로 초기화
    # deq : (현재 순서, 현재 라이언의 점수 별 화살 개수 배열)들을 담을 deque 
    # = deque([(0, [0 for i in range(len(apeachInfo))])])으로 초기화
    # res : 리턴값(배열)으로 아예 없거나, 여러개일 가능성이 있다
    # = []로 초기화
    
    maxGap = 0
    deq = deque([(0, [0 for i in range(len(apeachInfo))])])
    res = []
    
    while deq:
      
        # cnt : 현재 순서로, 현재 과녁 점수는 10-cnt
        # ryanInfo : 현재 라이언의 점수 별 화살 개수 배열
        
        cnt, ryanInfo = deq.popleft()
        
        # 1. 라이언이 화살을 모두 쏜 경우
        
        if sum(ryanInfo) == n:
          
            # apeachSum : 어피치의 전체 점수
            # ryanSum : 라이언의 전체 점수
            
            apeachSum, ryanSum = 0, 0
            
            # 점수 별 화살의 개수가 더 많은 사람이 점수를 가져간다
            for i in range(len(apeachInfo)):
                if not (apeachInfo[i] == 0 and ryanInfo[i] == 0):
                    if apeachInfo[i] >= ryanInfo[i]:
                        apeachSum += 10 - i
                    else:
                        ryanSum += 10 - i
                        
            # 1-1. 라이언이 이긴 경우,
            if apeachSum < ryanSum:
              
                # gap : 라이언과 어피치의 점수 차
                # gap이 maxGap 보다 클 때, res를 초기화하고 res에 현재 라이언의 점수 별 화살 개수 배열을 저장한다.
                # gap이 maxGap 과 같을 때, res에 현재 라이언의 점수 별 화살 개수 배열을 추가한다.
                
                gap = ryanSum - apeachSum
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                res.append(ryanInfo)
        
        
        
        # 2. 라이언이 쏜 화살 개수가 n보다 클 경우 거르기
        
        elif sum(ryanInfo) > n:
            continue
        
        
        
        # 3. 라이언이 화살을 모두 사용하지 않았는데, 현재 순서가 10인 경우
        # 남은 화살을 모두 써버리고 deq에 추가한다.
        
        elif cnt == 10:
            tmp = ryanInfo.copy()
            tmp[cnt] = n - sum(tmp)
            deq.append((cnt+1, tmp))
        
        
        
        # 위의 3가지 경우가 모두 아닌 경우
        # 라이언이 현재 점수에서 
        # 이기기 위해 어피치보다 1발 많이 쏘거나
        # 지기 위해 아예 화살을 쏘지 않는 두 경우를 deq에 추가한다.
        
        else:
            more = ryanInfo.copy()
            more[cnt] = apeachInfo[cnt]+1 
            deq.append((cnt+1, more))
            zero = ryanInfo.copy()
            zero[cnt] = 0
            deq.append((cnt+1, zero))
    
    return res

  
  
def solution(n, info):
    result = bfs(n, info)
    
    # result 배열의 원소가
    # 없는 경우 : 라이언이 어피치를 이길 수 있는 방법이 없으므로 [-1] 리턴
    # 1개인 경우 : 원소 하나를 리턴
    # 여러개인 경우 : 가장 낮은 점수를 더 많이 맞힌 경우를 리턴해야한다.
    # 과녁 점수가 높은 순으로 탐색해 배열에 추가해왔으므로, 가장 마지막 원소를 리턴
    
    if not result:
        return [-1]
    elif len(result) == 1:
        return result[0]
    else:
        return result[-1]
        
```

## 3. 주차 요금 계산
```python
# 문자열로 나타낸 시각을 정수형 분으로 변환하는 함수 (리턴값: 정수형 분으로 나타낸 시각값)
def hhmm_to_int(s):
    return int(s[:2])*60+int(s[3:])

  
  
# 주차요금 계산 함수 (리턴값: 주차요금)
def cal(time, fees):
  
    # time : 주차한 총 시간(분)
    # fees : [기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)]
    
    # 주차한 총 시간이 기본 시간보다 적거나 같은 경우,
    # 기본 요금 리턴
    
    if time <= fees[0]: 
        return fees[1]
      
    # 기본 시간을 초과했을 때,
    # 단위시간마다 단위요금 추가
    # 단, 초과 시간이 단위 시간에 나누어 떨어지지 않는 경우 올림 계산
    # over : 기본 시간 초과 시간 (분)
      
    over = time - fees[0]
    if not over % fees[2] == 0:
      over += fees[2]
    return fees[1] + over // fees[2] * fees[3]

  
  
def solution(fees, records):
  
    # fees : [기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)]
    # records : ["시각(시:분), 차량번호, 내역", ...]
    
    # time : time[i]는 차량번호 i가 주차한 총 시간(분)
    # = 차 번호는 네자리 양의 정수이므로 [0]*10000으로 초기화
    # entered : entered[i]는 차량번호 i가 입차한 시간(분)
    # = 입차하지 않은 경우를 -1로 나타내기 위해 [-1]*10000로 초기화
    # result : 차량 번호가 작은 자동차부터 청구할 주차 요금 배열
    
    time = [0]*10000
    entered = [-1]*10000
    result = []
    
    for r in records:
        hhmm, car, state = r.split()
        
        # 입차 및 출차 시각을 정수형 분으로 변환
        int_hhmm = hhmm_to_int(hhmm)
        
        # 차량 번호를 정수로 변환
        car = int(car)
        
        # 입차 : entered[차량번호]에 입차 시간 저장
        if state == "IN":
            entered[car] = int_hhmm
            
        # 출차 : 주차한 총 시간 저장(추가) 및 출차 상태로 변경
        else:
            time[car] += int_hhmm - entered[car]
            entered[car] = -1
            
    
    for i in range(10000):
      
        # 출차된 내역이 없는 경우,
        # 23:59에 출차된 것으로 간주
        if entered[i] != -1:
            time[i] += hhmm_to_int('23:59') - entered[i]
            
    for x in time:
        if x != 0:
            result.append(cal(x, fees))

    return result
  
```
