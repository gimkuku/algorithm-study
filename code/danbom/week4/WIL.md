# 1. 순위 검색
## 참고
https://whwl.tistory.com/193 <br />
https://www.daleseo.com/python-collections-defaultdict/

정확성은 풀리는데 효율성이 풀리지 않아 검색해보고 풀었다.. 어렵다.<br />
`defaultdict`도 알고는 있었는데 사용은 처음 해봤다. 편리한 것 같다.

## 풀이
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|info|지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열|["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]|
|query|개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열|["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]|

### 📁 솔루션 함수
함수 내 변수 설명
|이름|설명|예시|
|------|---|---|
|result|각 info, query가 매개변수로 주어질 때, 문의조건에 해당하는 사람들의 숫자를 순서대로 담은 배열|[1,1,1,1,2,4]|
|info_dict|지원자가 지원서에 입력한 4가지의 정보의 조합들과 그에 해당하는 사람의 점수가 담긴 딕셔너리|	defaultdict(<class 'list'>, {'': [50, 80, 150, 150, 210, 260], 'java': [80, 150], 'backend': [50, 80, 150, 260], 'junior': [80, 150], 'pizza': [150, 260], 'javabackend': [80, 150], 'javajunior': [80, 150], 'javapizza': [150], 'backendjunior': [80, 150], ...|
|info_key|지원자가 지원서에 입력한 4가지의 정보에 대한 배열|['java', 'backend', 'junior', 'pizza']|
|info_score|지원자가 획득한 코딩테스트 점수|150|
|tmp_key|지원자가 지원서에 입력한 4가지의 정보의 조합 중 하나|javabackend|
|query_score|개발팀이 원하는 코딩테스트 최소 점수|100|
|tmp_q|개발팀이 원하는 지원자의 정보 문자열|javabackendjuniorpizza|
|start, mid, end|이진 탐색에서 파생된 알고리즘으로 원하는 값 이상이 처음 나오는 위치를 찾는 `lower bound` 알고리즘을 사용하기 위한 변수들|0, (start + end) // 2, len(scores)|

```python
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    result = []
    info_dict = defaultdict(list)
    for i in info:
        i = i.split()
        info_key = i[:-1]
        info_score = int(i[-1])
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_score)
    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split()
        query_score = int(q[-1])
        q = q[:-1]

        for i in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        tmp_q = ''.join(q)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                result.append(len(scores) - start)
        else:
            result.append(0)
    return result
```
<br />

# 2. 합승 택시 요금
## 참고
https://bladejun.tistory.com/129 <br />
https://www.daleseo.com/python-heapq/ <br />
https://youtu.be/qaiuC3Q73-M <br />

다익스트라 알고리즘은 최단거리를 찾아주는 알고리즘이다. 방문했던 노드와 그 노드까지의 cost, 지금까지의 경로를 저장하고, 방문한 노드들로부터 이어지는 경로를 순서대로 탐색하며 가중치를 더해간다. 경로를 탐색하며 방문했던 노드를 또 방문하게 되는 경우 cost를 비교해 더 작은 값을 채택하며 더 큰 값을 가진 경로는 더 이상 탐색하지 않는다. <br />

블로그에선 먼저 `[cost, node]`가 담긴 리스트를 만들고, 이를 힙으로 변환하는 방법을 사용했는데 테스트 결과 **40ms ~ 4161ms**가 나왔다.
```python
# 기존 코드
heap = [[0, s]]
heapq.heapify(heap)
```
`heapq` 사용법을 찾아보며 리스트를 만들고 변환하는 방법이 아닌, 빈 리스트를 생성하고 여기에 `heapq` 모듈을 통해 원소를 추가하는 방법으로 테스트한 결과 **39ms ~ 4028ms**가 나왔다. 최소, 최대 값은 비슷하지만 대부분의 테스트 시간값들이 후자에서 더 작았다.
```python
# 바꾼 코드
heap = []
heapq.heappush(heap, [0, s])
```
<br />

최댓값을 주고 싶을 때, `sys`를 import해 `sys.maxsize`를 사용하면 되는 것을 알게되었다.
```python
visit = [sys.maxsize]*(n+1)
```
<br />

## 풀이
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|n|지점의 개수|6|
|s|출발지점|4|
|a|`A`의 도착지점|6|
|b|`B`의 도착지점|2|
|fares|지점 사이의 예상 택시요금|[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]|

### 📁 솔루션 함수
함수 내 변수 설명
|이름|설명|예시|
|------|---|---|
|result|A, B 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때, 예상되는 최저 택시요금|82|
|graph|각 지점 별 `(연결되어있는 지점, 그 지점까지의 택시요금)`들이 담긴 배열|[[], [[4, 10], [3, 41], [5, 24], [6, 25]], [[4, 66], [3, 22]], [[5, 24], [1, 41], [2, 22]], [[1, 10], [6, 50], [2, 66]], [[3, 24], [6, 2], [1, 24]], [[5, 2], [4, 50], [1, 25]]]|
|visit|각 노드 별 주어진 시작 지점에서부터의 최저 택시요금(길이 없는 경우, `sys.maxsize` 값이 담겨있다.)이 담겨 있는 배열|[9223372036854775807, 10, 66, 51, 0, 34, 35]|
|heap|`[cost, node]`들이 담긴 힙|[[50, 6], [66, 2]]|

```python
import sys
import heapq

def solution(n, s, a, b, fares):
    result = sys.maxsize
    graph = [[] for _ in range(n+1)]
    
    for i, j, cost in fares:
        graph[i].append([j, cost])
        graph[j].append([i, cost])
        
    def dijkstra(s, e):
        visit = [sys.maxsize]*(n+1)

        visit[s] = 0

        heap = []
        heapq.heappush(heap, [0, s])

        while heap:
            cost, node = heapq.heappop(heap)

            if cost > visit[node]:
                continue

            for new_node, new_cost in graph[node]:
                new_cost += cost

                if new_cost < visit[new_node]:
                    visit[new_node] = new_cost

                    heapq.heappush(heap, [new_cost, new_node])

        return visit[e]
            
    for i in range(1, n+1):
        result = min(result, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
        
    return result
```
<br />

# 3. 광고 삽입
## 참고
https://dev-note-97.tistory.com/156 <br />

블로그를 참고해서 푸는데도 아이디어를 이해하는 데에 시간이 오래 걸렸다.. 이번주 세문제 중엔 나 혼자 풀 수 있는 문제가 없었다.ㅠ

## 풀이
문자열 형식의 시간을 정수 형식의 초로, 정수 형식의 초를 문자열 형식의 시간으로 바꾸는 함수는 간단하므로 패쓰.
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|play_time|"죠르디"의 동영상 재생시간 길이|"02:03:55"|
|adv_time|공익광고의 재생시간 길이|"00:14:15"|
|logs|시청자들이 해당 동영상을 재생했던 구간 정보|["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]|

### 📁 솔루션 함수
함수 내 변수 설명
|이름|설명|예시|
|------|---|---|
|view|시간을 초로 쪼갰을 때, 각 초마다의 누적 시청자 수가 담긴 배열|[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  ...|
|section_view|반복문을 통해 시청자수가 가장 많은 구간을 탐색할 때, 해당 구간의 시청자수|2160|
|result|시청자들의 누적 재생시간이 가장 많이 나오는 곳의 시작 시각을 초로 나타낸 값|5459|

```python
def time_to_sec(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def sec_to_time(sec):
    h = sec // 3600
    h = '0' + str(h) if h < 10 else str(h)
    sec = sec % 3600
    m = sec // 60
    m = '0' + str(m) if m < 10 else str(m)
    sec = sec % 60
    s = '0' + str(sec) if sec < 10 else str(sec)
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)               
    view = [0 for _ in range(play_time + 1)]

    for l in logs:
        start, end = l.split('-')
        start = time_to_sec(start)
        end = time_to_sec(end)
        view[start] += 1
        view[end] -= 1

    # 구간별 시청자수 기록 : (i-1부터 i까지) 1초 동안의 시청자수
    for i in range(1, len(view)):
        view[i] += view[i - 1]

    # 모든 구간 시청자 누적 기록 : 0부터 i초 까지의 누적 시청자 수
    for i in range(1, len(view)):
        view[i] += view[i - 1]

    # 누적된 시청자수(view)로 가장 시청자수가 많은 구간 탐색
    section_view, result = 0, 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if section_view < view[i] - view[i - adv_time]:
                section_view = view[i] - view[i - adv_time]
                result = i - adv_time + 1
        elif section_view < view[i]:
            section_view = view[i]
            result = i - adv_time + 1

    return sec_to_time(result)
```
<br />
