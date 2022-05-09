# WIL : Week 4
4주차에 대한 WIL
## 최단거리 알고리즘
n이 노드 개수, e가 간선 개수라 하자.
- 플로이드-워셜 : 모든 경로의 최단거리를 구할 때 쓴다. O(n^3)
- 다익스트라 : 특정 시작지점의 최단거리를 구할 때 쓴다.
  - 매 번 모든 노드 검색하는 구현 -> 구현이 쉬움. O(n^2)
  - heap을 써서 구현 -> 구현이 어려움. O(eLogn)

언제 어떤 알고리즘이 쓰이는지 알고, 바로 구현할 수 있도록 미리 연습하자.

# kakao_72412 : 순위 검색
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/72412
## 😎 Solved Code
### 💻 Code

```python
from itertools import product
from bisect import bisect_left, bisect_right 

def count_by_range(array, left_value, right_value): 
    right_index = bisect_right(array, right_value) 
    left_index = bisect_left(array, left_value) 
    return right_index - left_index

def get_index(lang, position, career, food):
    return 3*3*3*lang + 3*3*position + 3*career + food

def store_data(lang, position, career, food, score, map_d, info_list):
    for l_, p_, c_, f_ in product([0,1], repeat=4): #(0,0,0,0) ~ (1,1,1,1) 16가지
        l, p, c, f = map_d[lang], map_d[position], map_d[career], map_d[food]
        info_list[get_index(l*l_, p*p_, c*c_, f*f_)].append(int(score))
    return

def solution(info, query):
    answer = []
    info.sort(key=lambda x : int(x.split(" ")[4]))
    map_d = {
        "-": 0,
        "cpp": 1,
        "java": 2,
        "python": 3,
        "backend": 1,
        "frontend": 2,
        "junior": 1,
        "senior": 2,
        "chicken": 1,
        "pizza": 2
    }
    info_list = [[] for _ in range(4*3*3*3)]
    for i in info:
        lang, position, career, food, score = i.split(" ")
        store_data(lang, position, career, food, score, map_d, info_list)
    
    for q in query:
        lang, _, position, _, career, _, food, score = q.split(" ")
        l, p, c, f = map_d[lang], map_d[position], map_d[career], map_d[food]
        idx = get_index(l,p,c,f)
        if not info_list[idx]:
            answer.append(0)
        else:
            count = count_by_range(info_list[idx], int(score), info_list[idx][-1])
            answer.append(count)
    
    return answer
```

### ❗️ 결과

성공

### 💡 접근

효율성 테스트 조건이 걸려있다. info는 50,000 이고 query는 100,000이다.

한 query당 시간복잡도가 O(info)라면, 총 시간복잡도가 O(info*query) = 50억이다.

따라서 한 query당 시간복잡도는 O(Log(info))가 되어야만 한다.

다시 문제를 보자. 각 query는 `[조건] X` 형태로 되어있다.

`[조건]`에 맞는 데이터를 뽑는 작업이 O(1)이 걸린다 하자. 그럼 그 중에서 코딩테스트 점수가  `X점` 이상인 데이터를 또다시 추출하는 작업은 반드시 `O(Log(info))` 이하로 걸려야 한다.

이 말은 `X점` 이상인 데이터를 계산하는 과정은 `이진탐색` 알고리즘을 써야한다는 뜻이다.

다음은 실제 구현에 대한 설명이다.

1. info를 순회하며 스코어 점수에 따라 오름차순 정렬한다. O(info)
2. 다시 info를 순회하며 `info_list` 에 데이터를 담는다. O(info)
3. query를 순회하며 조건에 맞는 데이터 리스트를 `info_list` 에서 가져온 뒤, `X점` 이상인 데이터를 `이진탐색` 으로 구한다. O(info*query)

2번에서 `info_list`에 데이터를 담는 과정을 다음과 같이 구현했다.

예를 들어, `java backend junior pizza 150` 라는 데이터가 있다 하자.

이 데이터는 다음과 같은 query(score 제외)에 의해 검색될 수 있다.

- `java and backend and junior and pizza`
- `java and backend and junior and -`
- `java and backend and - and pizza`
- ...
- `- and - and - and -`

즉, 2*2*2*2 = 16가지의 query에 의해 검색될 수 있다. 그럼 가능한 모든 쿼리의 경우의 수 4*3*3*3=108 크기의 빈 리스트를 만들고, 위의 16가지의 대응되는 빈 리스트에 데이터를 넣으면 된다.

이를 위해 다음과 같은 방식으로 규칙을 정했다.

```python
map_d = {
        "-": 0,
        "cpp": 1,
        "java": 2,
        "python": 3,
        "backend": 1,
        "frontend": 2,
        "junior": 1,
        "senior": 2,
        "chicken": 1,
        "pizza": 2
    }
```

만약 `java and backend and junior and pizza` 라면, 3*3*3*java + 3*3*backend + 3*junior + pizza = 3*3*3*2 + 3*3*1 + 3*1 + 2 = 68이다. 이는 0~107까지의 query 조합중 68번째에 해당된다는 뜻이며, index 위치로 생각하면 된다.

마찬가지로 `- and - and - and -` 는 0으로, 0~107중 0번째 쿼리 조합이다.

실제 데이터는 전부 담지는 않고 코딩테스트 score만 담았다. 1번에서 info를 점수에 대해 오름차순 정렬했기 때문에 info_list 내의 108가지 모든 리스트는 오름차순 정렬되어있다.

그리고 이진탐색 라이브러리 bisect를 사용한 count_by_range를 이용하여 X점 이상인 데이터 개수를 세었다.

## 🥳 문제 회고

상당히 오래 고민했던 문제. `[조건] X` 에 대해 X점 이상인 데이터 개수를 세는 작업이 반드시 이진탐색으로 O(LogN)에 해결해야 한다고 생각하고 접근했다.

그런데 문제 해결 전까지 생각한 방법으로는 [조건]을 처리하고 남은 데이터들이 오름차순 정렬이 되어있지 않았다. 그렇다고 quert 처리마다 오름차순 정렬 하면 백프로 시간초과였다. 그런데 처음부터 오름차순 정렬해도 [조건] 처리를 하면 뒤죽박죽 순서가 섞였다.

여기에서 너무 막혀서 카카오 문제 해설을 슬쩍 봤다... 해답은 모든 query 조합에 대한 경우의수를 미리 다 정의하는 것 이었다;; 

브루트포스 컨셉으로 문제 해결할 생각을 못했는데, 처음부터 브루트포스로 접근하고 안 될 경우 dp나 다른 알고리즘으로 접근하는게 올바른 사고의 흐름같다... 반성하게 된 문제

### Ref

[https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/](https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/)

# kakao_72413 : 합승 택시 요금
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/72413
## 😎 Solved Code

### 💻 Code

```python
def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)
    distance = [[INF] * (n+1) for _ in range(n+1)] # 비용 INF로 초기화
    
    for i in range(n+1):
        distance[i][i] = 0 # i<->i 비용 0으로 초기화
    
    for i, j, fare in fares: # i<->j 비용이 있으면 해당값으로 갱신
        distance[i][j] = fare
        distance[j][i] = fare
    
    # 플로이드-워셜
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                min_val = min(distance[i][j], distance[i][k] + distance[k][j])
                distance[i][j] = min_val
                distance[j][i] = min_val
    
    answer = INF
    # s->i(합승) + i->a(a 따로) + i->b(b 따로) 최솟값
    for i in range(1,n+1):
        answer = min(distance[s][i] + distance[i][a] + distance[i][b], answer)

    return answer
```

### ❗️ 결과

성공

### 💡 접근

cost(x,y)는 x와 y 사이의 최소요금이라 하고 문제 조건대로 s, a, b가 주어졌을 때

cost(s→i) + cost(i→a) + cost(i→b) 의 최솟값이 답일것이다. (i는 1 ~ n 가능)

이 말은 임의의 x,y에 대해 cost(x,y)를 전부 알아야 한다. 즉 모든 x,y 조합에 대한 최소비용을 구할 수 있는 `플로이드-워셜` 알고리즘이 적당하다.

- 2차원 리스트 distance를 전부 INF(1e9)로 초기화한다
- 자기 자신에서 자기 자신으로 향하는 경우는 0으로 갱신한다(대각행렬. distance[i][i])
- fares에 나온 요금 정보를 distance에 갱신한다
- 플로이드-워셜로 distance를 전부 구한다
- i 를 1부터 n까지 순회하며, `distance[s][i] + distance[i][a] + distance[i][b]`의 최솟값을 구한다

효율성 테스트가 있지만 노드 개수가 200이므로 O(n^3)인 플로이드-워셜로 해결이 가능하다.

## 🥳 문제 회고

최단거리 알고리즘 복습을 안해서 다익스트라, 프림, 크루스칼, 플로이드-워셜 알고리즘을 다시 공부하고 풀었다. 자주 나오는 유형인 것 같으니 상황에 맞게 알고리즘을 선택해서 빠르게 구현해야겠다.

# kakao_72414 : 광고 삽입
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/72414
## 😎 Solved Code

### 💻 Code

```python
def hhmmss_to_seconds(hhmmss):
    hh, mm, ss = hhmmss.split(":")
    return int(hh)*3600 + int(mm)*60 + int(ss)

def seconds_to_hhmmss(s):
    hh = str(s//3600)
    mm = str(s%3600//60)
    ss = str(s%3600%60)
    if len(hh) == 1:
        hh = '0' + hh
    if len(mm) == 1:
        mm = '0' + mm
    if len(ss) == 1:
        ss = '0' + ss
    return hh+':'+mm+':'+ss

def get_answer(S, n, l):
    if n == l:
        return 0
    tail_i = 0
    head_i = l-1
    max_count = sum(S[0:l])
    sub_sum = sum(S[0:l])
    start = 0
    while head_i+1 <= n:
        if sub_sum + S[head_i+1] - S[tail_i] > max_count:
            start = tail_i + 1
            max_count = sub_sum + S[head_i+1] - S[tail_i]
        sub_sum += S[head_i+1] - S[tail_i]
        head_i += 1
        tail_i += 1
    return start

def solution(play_time, adv_time, logs):
    answer = ''
    cumulative_sum = [0]*360001
    play_time = hhmmss_to_seconds(play_time)
    adv_time = hhmmss_to_seconds(adv_time)
    
    # 누적합 계산을 위한 시작, 끝 기록
    for log in logs:
        start,end = log.split("-")
        start = hhmmss_to_seconds(start)
        end = hhmmss_to_seconds(end)
        cumulative_sum[start] += 1
        cumulative_sum[end] += -1
    
    # 누적합 계산
    for i in range(1,play_time+1):
        cumulative_sum[i] += cumulative_sum[i-1]
    start_seconds = get_answer(cumulative_sum, play_time, adv_time)
    answer = seconds_to_hhmmss(start_seconds)
    return answer
```

### ❗️ 결과

성공

### 💡 접근

00:00:00 ~ 99:59:59 를 초로 표현하면 0 ~ 359999 다. 그럼 길이 360000 짜리 cumulative_sum 리스트에 매 초마다 몇 명의 시청자가 시청하고 있는지 카운트를 하면 된다.

근데 logs 길이가 30만이라서 단순한 카운팅은 시간초과가 될 것이다. 시작시각, 끝시각만 기록하는 `누적합 알고리즘` 을 이용해 O(N)에 누적 시청자를 구한다.

조심해야하는게 카운팅 범위가 [ Start, End ] 가 아닌, [ Start, End ) 이다. (종료 시각은 카운팅 제외)

마지막으로 영상 길이를 초로 변환하여 cumulative_sum를 순회하며 가장 시청자가 많은 구간의 시작시간을 구한다.

예를 들어 길이가 5라하고, sub_sum = sum(S[0:5]) 이라 하자.(구간 0 ~ 4까지 시청자 합)

그 다음에는 sub_sum과 sub_sum + S[5] - S[0] 를 비교해 최대값을 저장하면된다.

위와 같은 방법으로 계속해서 순회를 하며, 다음 원소(head)와 sub_sum의 첫 원소(tail)을 각각 더하고 빼며 O(N)에 비교를 마친다.

## 🥳 문제 회고

누적합 문제를 풀었기 때문에 접근방법은 금방 떠올랐다. 그런데 인덱스 관련해서 실수가 너무 많아서 구현에 상당히 오래걸렸다. 예를 들어 시청시각 end도 시청자 카운팅을 한다던지... 시간 초과 안뜨게 누적합 알고리즘을 써야하며, 구현도 인덱스를 신경써야했던 까다로운 문제였다!