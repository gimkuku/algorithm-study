# WIL : Week 2
2주차에 대한 WIL
## imos 알고리즘
누적합을 빠르게 구할 수 있는 알고리즘이다.

아래 예시 상황을 보자
```
0에서 T까지 운영하는 가게가 있다. 가게에 Q명의 손님이 방문한다. 각각의 손님 i는 Start(i)에 입장하여, End(i)에 퇴장한다. 이 때, 0<=Start(i)<End(i)<=T 이다. 가장 많이 방문했을 때 손님 수는?
```

단순히 range(Q)에 대해 순회하며 Start(i) ~ End(i) 까지 1씩 더한다면
- Start(i) ~ End(i) 까지 더하는 작업 : O(T)
- range(Q)에 대해 순회하는 작업 : O(Q)

따라서 시간복잡도는 `O(TQ)`이다.

imos 알고리즘을 적용하여 `O(T+Q)`의 시간복잡도에 문제를 해결할 수 있다.
imos 알고리즘의 핵심은 `시작 지점`과 `끝 지점`만 기록한다는 것이다.

예를 들어 길이 T가 10이며, 1번 손님은 [1,3], 2번 손님은 [2,5] 만큼 머물렀다 하자.
- 1번 손님 기록 : [0,1,0,0,-1,0,0,0,0,0,0] (1번 인덱스에 +1 / 3+1번 인덱스에 -1)
- 2번 손님 기록 : [0,1,1,0,-1,0,-1,0,0,0,0] (2번 인덱스에 +1 / 5+1번 인덱스에 -1)

이제 0부터 10까지 순회하며 누적하며 더한다
- [0,1,2,2,1,1,0,0,0,0,0]

이렇게 간단하게 누적합을 계산하여 문제를 해결할 수 있다. 이를 일반화 하면 다음과 같다.

- range(Q)만큼 순회하며 Start(i) 인덱스의 값을 +1, End(i)+1 인덱스 값을 -1 한다 : O(Q)
- 순회를 마치면 0 ~ T까지 누적합을 구한다 : O(T)

따라서 시간복잡도는 `O(T+Q)`이다.

2차원 상에서도 동일한 방법으로 누적합을 계산할 수 있으며, 2차원 NxM matrix에 대해 O(Q+NM)의 시간복잡도를 갖는다.
주의 할 점은 `좌->우`로 Row에 대한 누적합을 구한 뒤, 다른 축에 대해 `상->하`로 Col에 누적합 계산을 마무리 한다.


# kakao_92334 : 신고 결과 받기
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92334
## Solved Code
```python
def solution(id_list, report, k):
    answer = []
    report_dict = {}
    
    # 신고 정보 딕셔너리 초기화
    for i in id_list:
        tmp = dict()
        tmp['count'] = 0  # 누적 신고 횟수
        tmp['report_from'] = [] # 나를 신고한 사람
        tmp['report_to'] = [] # 내가 신고한 사람
        report_dict[i] = tmp
        
    for rep in report:
        r_from, r_to = rep.split(' ')
        # 처음 신고한다면
        if r_to not in report_dict[r_from]['report_to']:
            report_dict[r_from]['report_to'].append(r_to)
            report_dict[r_to]['report_from'].append(r_from)
            report_dict[r_to]['count'] += 1
    
    # 정지당한 계정 추출
    blocked_list = []
    for i, info in report_dict.items():
        if info['count'] >= k:
            blocked_list.append(i)
    
    # 집합으로 만듬
    blocked_set = set(blocked_list)
    
    # 발송할 메일 횟수 계산
    for _, info in report_dict.items():
        report_to = set(info['report_to'])
        answer.append(len(report_to&blocked_set)) # 교집합 원소 개수
    return answer
```
### 결과
성공
### 접근
- 신고 정보를 다음과 같이 report_dict에 저장한다. (id list 순서대로 저장)
```python
{
  "muzi" : {
    "count" : 0, # 내가 신고당한 누적 횟수
    "report_from" : [], # 나를 신고한 id 리스트
    "report_to" : [], # 내가 신고한 id 리스트
  },
  ...
}
```
- report 문자열 리스트 정보를 읽어와 `report_from`, `report_to`로 split 한다
- `if r_to not in report_dict[r_from]['report_to']`로 `report_from`이 `report_to`를 처음 신고하는 경우에만 정보를 갱신한다
- 갱신할 정보는 신고당한 횟수와 누가 누구를 신고했는지 양방향으로 담는다
- 정지당한 계정 리스트를 추출하여 set으로 만든다
- report_dict를 순회하며 내가 신고한 id들이 담긴 `report_to`를 추출해 set으로 만든다
- 위에서 만든 두 set을 교집합 연산하여 개수를 answer에 append 한다

## 92334 : 신고 결과 받기 문제 회고
처음 주어진 id_list 순서대로 답을 구해야 하기 때문에, 처음부터 id_list대로 정보를 저장했다.
내가 신고한 유저 집합과 정지당한 유저 집합의 교집합 연산을 통해 발송할 메일 개수를 구했다.
조건대로 구현하기만 하면 되는 비교적 간단한 문제였던 것 같다.

# kakao_92344 : 파괴되지 않은 건물
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92344
## Solved Code
```python
def solution(board, skill):
    answer = 0
    height, width = len(board), len(board[0])
    matrix = [[0] * (width+1) for _ in range(height+1)] # (height+1) x (width+1) matrix

    # 시작 좌표, 끝 좌표 기록 : O(len(skill))
    for type, r1, c1, r2, c2, degree in skill:
        degree *= (-1) if type == 1 else 1
        matrix[r1][c1] += degree
        matrix[r2+1][c2+1] += degree
        matrix[r1][c2+1] -= degree
        matrix[r2+1][c1] -= degree
        
    # 누적 합 계산 : O(width*height)
    # 가로 방향 (좌->우) 누적합 계산
    for i in range(1,width+1):
        for j in range(height+1):
            matrix[j][i] += matrix[j][i-1]
    
    # 세로 방향 (상->하) 누적합 계산
    for j in range(1,height+1):
        for i in range(width+1):
            matrix[j][i] += matrix[j-1][i]
    
    # 파괴되지 않은 건물 개수 계산
    for y in range(height):
        for x in range(width):
            if board[y][x] + matrix[y][x] > 0 :
                answer += 1
    return answer
```
### 결과
성공
### 접근
누적합 문제를 빠른 시간복잡도에 풀 수 있는 `imos` 알고리즘으로 해결했다.

## 92344 : 파괴되지 않은 건물 문제 회고
도저히 나 스스로는 해결하기 어려웠던 문제,,, 문제 해결까지의 과정을 회고해보겠다.

대부분 문제를 읽고 바로 naive한 해결법이 떠올랐을 것이다. 그런데 첫 줄에 `[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]` 라는 문구를 보고
naive하게 접근하면 안된다는 걸 알았다. 그래도 궁금해서 바로 떠오른 해결법대로 구현을 해봤다.

skill을 순회하며 좌표값들을 받아 board를 좌표의 영역만큼 매 번 순회하며 더하거나 빼는 식으로 구현했다. 결과는 `정확성 100점 효율성 0점으로 실패`.
그도 그럴 것이 시간복잡도가 `O(N*M*skill길이)`, 대략 25만x1000x1000이기 때문이다.

두 가지로 접근하며 생각해봤다.

1. skill을 순회하며 매 번 좌표에 값을 더하는 과정을 O(1)로 구현하자. 그럼 최종 시간복잡도는 O(skill길이) 일 것.
2. skill을 순회하며 좌표값들을 저장한 후, 마지막에 board 전체를 순회하며 한 번에 더하자. 그럼 최종 시간복잡도는 O(skill길이 + N*M) 일 것.

처음에는 첫번째 접근에만 매달렸다. 우리는 시각적으로 행렬 위에 직사각형 면적 단위로 덧셈을 할 수 있지만 컴퓨터는 기본적으로 하나하나 순회를 해야 한다. 이 과정에서 순회를 빼고 면적 단위로 O(1)에 덧셈을 할 방법이 있을거라 생각했다. 그런데 도저히 방법이 떠오르지 않았다.

두번째 접근은 가능한 방법인가 싶어서 의문이 들었는데 옆에서 같이 공부하던 현재형이 문제에 대해 검색해보고 `imos`알고리즘을 활용하면 가능하다고 힌트를 줬다. `imos` 알고리즘을 검색해보자마자 해결법이 떠올랐고 바로 구현해서 문제 해결에 성공했다. 알고리즘 설명글은 아래 레퍼런스에 남겨뒀다.

돌이켜보면 imos 알고리즘의 기본 컨셉은 혼자 생각하기 어려웠을 것 같다. 그런데 1차원에서 적용하는 개념을 2차원으로 확장하는 컨셉은 조금 더 고민해본다면 떠올렸을수도 있겠다 싶었다. 알고리즘 수업 때 1차원 배열 상에서 Maximum Subsequence Sum을 구하는 로직을 2차원으로 확장시키는 방법을 배웠는데 컨셉이 유사했다. 2차원 matrix를 1차원으로 정사영시켜 해결했던 방법이다. 주어진 문제의 해결 과정에서도 2차원 matrix를 1차원 방향으로 누적합을 구하며 정사영 시키는 느낌이 들었다.

### Ref
[imos 알고리즘 소개](https://driip.me/65d9b58c-bf02-44bf-8fba-54d394ed21e0)

# kakao_92343 : 양과 늑대
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92343
## Solved Code
```python
def update_candidates(candidates, graph, visited):
    # 현재 인접한 노드 (candidates)에 대해 방문한 노드(visited)를 고려해 새로운 인접 노드 리스트 계산
    # ex. 예시 1 경우에서 candidates : {1,8}, visited: {0,1} -> return {2,4,8}
    candidates_set = set(candidates)
    for i in visited:
        candidate_set = set(graph[i])
        candidates_set |= candidate_set
    candidates_set -= set(visited)
    return list(candidates_set)

def dfs(candidates, graph, sheep, wolves, info, visited):
    '''
    candidates : 인접 노드 리스트
    graph : 그래프 정보
    sheep : 현재까지 모은 양의 수
    wolves : 현재까지 따라온 늑대 수
    visited : 현재까지 방문한 노드
    '''
    global MAX_NUM
    
    # 방문한 적 없는 인접 노드에 양이 존재하지 않을 때까지 노드 방문 후 인접 노드 리스트 갱신
    new_sheep_num = 0
    while True:
        flag = True
        for i in candidates:
            if info[i] == 0: # 양이 있다면
                new_sheep_num += 1 # 모을 수 있는 양 1마리 추가
                visited.append(i) # 해당 노드는 방문처리
        candidates = update_candidates(candidates, graph, visited) # 새로운 인접 노드 리스트 갱신
        for i in candidates:
            if info[i] == 0: # 만약 갱신된 인접 노드에 양이 존재한다면
                flag = False # while문 다시 수행
        if flag :
            break # 더이상 인접 노드에 양이 없다면 반복문 탈출
    
    # 더 이상 이동할 노드가 없거나 or 이동시 늑대에게 모두 잡아먹힌다면 return
    if not candidates or sheep + new_sheep_num - wolves == 1:
        if  MAX_NUM < sheep + new_sheep_num: # MAX_NUM 과 비교 후 갱신
            MAX_NUM = sheep + new_sheep_num
        return
    
    # 인접한 노드에 늑대밖에 없는 상황. 탐색할 후보 노드(candidates) 업데이트 후 탐색
    for i in candidates:
        new_candidates = update_candidates(candidates, graph, visited + [i]) # i 노드를 방문했다 가정하고 인접노드 갱신
        dfs(new_candidates, graph, sheep + new_sheep_num, wolves + 1, info, visited + [i])
    
    return

def solution(info, edges):
    global MAX_NUM
    graph = [[] for _ in range(18)]
    
    # 그래프 정보 저장
    for from_node, to_node in edges:
        graph[from_node].append(to_node)
        graph[to_node].append(from_node)
    
    # 최대 양 개수 초기화 (시작시 1마리)
    MAX_NUM = 1
    dfs(graph[0],graph,1,0,info,[0])
    return MAX_NUM
```
### 결과
성공
### 접근
테스트 케이스와 문제 조건을 보며 어떤 경우에 최대한 많이 양을 모을 수 있는지 고민했다.
다음괴 같은 사실들을 발견했다.

- 현재 위치에서 인접한 양들은 전부 모아야한다
- 늑대가 있는 노드로 이동할 때 `"모인 양 > 따라온 늑대 + 1"` 일때 만 이동할 수 있다
- 위 두가지 사실을 만족시키며 이동 가능한 모든 노드를 탐색하여 답을 구해야 한다

도식화하면 다음과 같다
![양과늑대](https://user-images.githubusercontent.com/48646015/158808895-2517eee8-2f5a-4dd1-aeae-e1a717e02b52.png)

다음은 문제 해결을 위한 접근이다.
- graph를 다음과 같은 형태로 저장한다
```python
[
  [1,4,6], # 0번 노드와 인접한 노드들
  [0,2,3], # 1번 노드와 인접한 노드들
  ...
]
```
- 지금까지 최대로 모인 양의 수 MAX_NUM = 1로 초기화 한다
- 0번 노드 방문을 시작으로 dfs를 호출한다.

아래부터는 dfs의 작업 내용이다.
- 지금까지 방문한 노드들의 인접 노드에 양이 존재하지 않을 때 까지 모든 노드를 방문한다. `(가능한 최대의 양을 모은다)`
- `update_candidates` 메소드로 방문한 노드들의 인접 노드 리스트를 계산하여 반환한다.
    - 합집합, 차집합 연산을 이용하여 구현했다
    - 이미 방문한 적 있는 인접 노드는 제외시킨다
- 위의 과정을 마치고 나면 아래 세 가지중 하나이다
    1. 방문한 적 없는 노드가 더이상 없거나
    2. 방문한 적 없는 인접 노드에 늑대만 존재하며, 이동 시에 양이 모두 잡아먹힌다
    3. 방문한 적 없는 인접 노드에 늑대만 존재하며, 이동 시에 양이 모두 잡아먹히지 않는다
- 1,2번의 경우 : `MAX_NUM`과 지금까지 모은 양을 비교하여 `MAX_NUM`을 갱신한다
- 3번의 경우 : 인접노드를 dfs 재귀 호출을 통해 방문한다

재귀 호출이 전부 끝나면 MAX_NUM을 정답으로 제출한다.

## 92344 : 양과 늑대 문제 회고
이번 주차에서 가장 오래걸렸던 문제. 그래프로 주어졌기 때문에 dfs를 통해 가능한 모든 경우의 수를 탐색해야 할 것 같았다. 하지만 말 그대로 모든 경우의 수를 탐색하면 Recursion depth 이슈가 발생할 것 같았다.

그래서 고민한 결과 찾은 팩트가 `늑대를 만나러 가기 전까지 가능한 모든 양을 모으는 것`이었다. 지금 생각해보면 현재 노드로부터 인접노드를 우선적으로 탐색하는 bfs 개념인 것 같다.

가능한 많은 양들을 모은 상황에서(인접한 노드들이 늑대만 남았을 때) 호기롭게 늑대를 만나러 가면 된다. 이 과정은 `dfs`로 재귀 호출로 구현했다.

또 굳이 방문하면 모두 양들이 잡아먹히는 경우는 return해서 dfs 호출 횟수를 줄였다.

이렇게 적고 보면 되게 간단하게 푼 것 같은데 오랜만에 재귀함수를 구현해서 그런지 너무 오래걸렸다ㅠㅠ... 그리고 `MAX_NUM` 이라는 global 변수를 처음 써봤는데, 처음엔 이 전역 변수 없이 구현해서 최대로 모은 양 비교시에 애를 먹었다.

물론 충분한 시간이 주어져서 풀었지만 실전에서 빠르게 풀기 위해 그래프 탐색 유형을 많이 다뤄봐야할 것 같다.