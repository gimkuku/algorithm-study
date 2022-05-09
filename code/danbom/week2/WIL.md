# 1. 양과 늑대
## 접근
가능한 모든 상황을 고려하는 깊이 탐색을 하되, 양이 모두 잡아먹히는 경우는 조건문으로 거르자.

## 풀이
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|info|각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열, ( `0` : 양, `1` : 늑대 )|[0,0,1,1,1,0,1,0,1,0,1,1]|
|edges|2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 ( [`부모 노드 번호`, `자식 노드 번호`] 형태 )|[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],...]|

`info`를 따라 양의 수, 늑대의 수를 더해가며 늑대의 수가 양의 수보다 많거나 같아질 경우를 거를 수 있고,<br />
`edges`를 통해 특정 노드 번호에 대한 다음 노드 번호들을 알 수 있다.

### 📁 필요한 함수들
1. **입력 받은 노드 번호 다음으로 올 수 있는 노드 번호들을 구하는 함수**<br /><br />
    함수 입출력 설명
    |이름|설명|예시|
    |------|---|---|
    |node|`입력` 입력 받은 기준 노드 번호|0|
    |nextNodes|`리턴` 기준 노드 다음에 올 수 있는 노드 번호들|[1, 8]|
    ```python
    def getNextNodes(edges, node):
        nextNodes = []

        for e in edges:
            i,j = e # 예) e : [0, 1] / i : 0 / j : 1
            if node == i:
                nextNodes.append(j)

        return nextNodes
    ```
    <br />
2. **깊이 탐색 함수**<br /><br />
    함수 입출력 설명
    |이름|설명|예시|
    |------|---|---|
    |sheep, wolf|`입력` 각각 현재까지의 양의 수, 늑대의 수|0|
    |cnt|`입력` 현재 노드 번호|0|
    |path|`입력` 현재까지의 path나 다음에 갈 노드 번호 등을 담을 리스트 |[0, 1, 8, 7, 2, 9, 4]|
    |maxSheep|`리턴` 각 노드를 방문하면서 모을 수 있는 최대 양의 수|5|

    ```python
    def dfs(info, edges, sheep, wolf, cnt, path):
        if info[cnt]:
            wolf += 1
        else:
            sheep += 1
        if sheep <= wolf:
            return 0 # 양이 모두 잡아먹히는 경우는 조건문으로 거르기

        maxSheep = sheep

        for p in path:
            for n in getNextNodes(edges, p):
                if n not in path:
                    path.append(n)
                    maxSheep = max(maxSheep, dfs(info, edges, sheep, wolf, n, path))
                    path.pop()

        return maxSheep
    ```
    ```python
    # 중간 코드를 이런식으로 바꿔보면
    if sheep <= wolf:
        print("\nWARNING! 늑대가 양보다 많아져따!")
        return 0

    maxSheep = sheep
    for p in path:
        for n in getNextNodes(edges, p):
            if n not in path:
                path.append(n)
                print("현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : " + str(path) + "\n양 : " + str(sheep) +", 늑대 : " + str(wolf) + " 니까 다음 노드로 가자!")
                maxSheep = max(maxSheep, dfs(info, edges, sheep, wolf, n, path))
                path.pop()
                print("못가니까 전 노드로 돌아가 다른 노드를 탐색하자\n현재까지의 path : " + str(path) + "\n")
    ```
    ```
    Output >>
    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1]
    양 : 1, 늑대 : 0 니까 다음 노드로 가자!
    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8]
    양 : 2, 늑대 : 0 니까 다음 노드로 가자!
    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8, 2]
    양 : 2, 늑대 : 1 니까 다음 노드로 가자!

    WARNING! 늑대가 양보다 많아져따!
    못가니까 전 노드로 돌아가 다른 노드를 탐색하자
    현재까지의 path : [0, 1, 8]

    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8, 4]
    양 : 2, 늑대 : 1 니까 다음 노드로 가자!

    WARNING! 늑대가 양보다 많아져따!
    못가니까 전 노드로 돌아가 다른 노드를 탐색하자
    현재까지의 path : [0, 1, 8]

    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8, 7]
    양 : 2, 늑대 : 1 니까 다음 노드로 가자!
    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8, 7, 2]
    양 : 3, 늑대 : 1 니까 다음 노드로 가자!
    현재까지의 path와 다음에 갈 노드 번호(마지막 원소) : [0, 1, 8, 7, 2, 4]
    양 : 3, 늑대 : 2 니까 다음 노드로 가자!
    ```

3. **솔루션 함수**<br />

    ```python
    def solution(info, edges):
        sheep = 0
        wolf = 0
        cnt = 0
        path = [0] # 항상 루트 노드(0번 노드)부터 시작
        answer = dfs(info, edges, sheep, wolf, cnt, path)

        return answer
    ```
    
<br />

# 2. 파괴되지 않은 건물
## 접근
브루트 포스로 풀 경우 시간 복잡도가 O(N * M * K)가 되어 효율성 테스트케이스에서 시간 초과가 발생한다.
2차원 배열에서 구간의 변화를 효율적으로 처리할 수 있는 방법을 찾아야한다.

## 풀이
### 📁 사전 지식
목표 : 2차원 배열에서 구간의 변화 효율적으로 처리하기

1\. 1차원 배열 효율적으로 처리하기

- `[1,2,4,8,9]` 배열에서 0번째 원소부터 3번째 원소까지 `-2`의 변화를 주고 싶을 때, 가장 쉬운 방법은 반복문을 사용하는 방법이다. 이 경우, 시간복잡도가 O(N)이 된다. 그렇다면, 누적합이라는 개념을 도입해보자. 누적합을 이용하게 되면, 시간복잡도는 O(1)이 된다.

- 0번째 원소부터 3번째 원소까지 `-2`의 변화를 주고 싶을 때, `[-2,0,0,0,2]`의 새로운 배열을 생성한다. 이 배열의 경우 앞에서부터 누적하면 `[-2,-2,-2,-2,0]`이 된다. 이 배열을 초기 배열과 더하면 원하는 결과를 얻을 수 있다.

- 따라서, 누적합의 원리는 1차원 배열의 a번째 원소부터 b번째 원소까지 c만큼 변화를 준다했을 때, 새로운 배열의 a번째 원소에 c를 더하고, b+1번째 원소에 c를 빼면 된다. 이 방법을 문제에 적용했을 경우, 시간복잡도는 O(N * K)가 되는데 이 경우에도 시간 초과 문제가 발생한다.

2\. 2차원 배열로 아이디어 확장하기

- 2차원 배열에서 (0,0)부터 (2,2)까지 n만큼 변화시켜보자.
먼저, 배열의 행만 보고 1번의 아이디어를 한 행씩 적용시켜 보면
    |n|0|0|-n|
    |:---:|:---:|:---:|:---:|
    |n|0|0|-n|
    |n|0|0|-n|

- 위 행렬을 열을 기준으로 보았을 때, 첫번째 열의 0번째부터 2번째까지 n만큼의 변화가, 마지막 열의 0번째부터 2번째까지 -n만큼의 변화가 있는 것을 알 수 있다. 여기에도 1번의 아이디어를 적용시키면

    |n|0|0|-n|
    |:---:|:---:|:---:|:---:|
    |0|0|0|0|
    |0|0|0|0|
    |-n|0|0|n|

- 이런 방식으로 누적합 배열을 구할 수 있다. 그리고 이 때의 시간복잡도는 행,열 각각 누적합해줘야하기 때문에 O(N * M)이 된다.

- 위와 같은 방법으로 skill의 한 원소를 O(1)만에 처리할 수 있고, skill이 총 K개 인 경우, 시간복잡도는 O(K)가 된다. 따라서, 전체 시간복잡도는 O(K + N * M)이 된다.

### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|board|건물의 내구도를 나타내는 2차원 정수 배열|[[1,2,3],[4,5,6],[7,8,9]]|
|skill|적의 공격 혹은 아군의 회복 스킬을 나타내는 2차원 정수 배열로 각 행은 [type, r1, c1, r2, c2, degree]형태|[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]|

### 📁 솔루션 함수
|이름|설명|예시|
|------|---|---|
|answer|적의 공격 혹은 아군의 회복 스킬이 모두 끝난 뒤 파괴되지 않은 건물의 개수|6|
|prefixSum|`board`에 대한 누적합 배열|[[-2, -2, 0, 0], [-2, -6, -4, 0], [100, -4, -4, 0], [0, 100, -4, -4]]|
|type|1일 경우는 적의 공격, 2일 경우는 아군의 회복 스킬을 의미|1|
|r1, c1, r2, c2, degree | (r1, c1)부터 (r2, c2)까지 직사각형 모양의 범위 안에 있는 건물의 내구도를 degree 만큼 낮추거나 높인다는 뜻 | 1,1,2,2,4 |

```python
def solution(board, skill):
    answer = 0
    prefixSum = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
 
    for type, r1, c1, r2, c2, degree in skill:
        prefixSum[r1][c1] += degree if type == 2 else -degree
        prefixSum[r1][c2 + 1] += -degree if type == 2 else degree
        prefixSum[r2 + 1][c1] += -degree if type == 2 else degree
        prefixSum[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    for i in range(len(prefixSum) - 1):
        for j in range(len(prefixSum[0]) - 1):
            prefixSum[i][j + 1] += prefixSum[i][j]

    for j in range(len(prefixSum[0]) - 1):
        for i in range(len(prefixSum) - 1):
            prefixSum[i + 1][j] += prefixSum[i][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += prefixSum[i][j]
            if board[i][j] > 0: answer += 1

    return answer
```


<br />

# 3. 신고 결과 받기
## 접근
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리되니 중복을 제거해주자.

## 풀이
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|id_list|이용자의 ID가 담긴 문자열 배열|["muzi", "frodo", "apeach", "neo"]|
|report|각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열|["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]|
|k|이용자의 정지 기준이 되는 신고 횟수|2|

`id_list`에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 리턴하면 되므로,<br />
`answer`를 `id_list`의 길이만큼 0으로 이루어진 배열로 초기화한다.<br />
동일한 유저에 대한 신고 횟수를 1회로 처리하기 위해 `set(report)`로 중복을 제거해준다.

### 📁 솔루션 함수
|이름|설명|예시|
|------|---|---|
|answer|각 유저별로 처리 결과 메일을 받은 횟수가 담긴 배열|[2,1,1,0]|
|reported|각 유저의 id와 유저별로 신고 받은 횟수가 담긴 딕셔너리|{'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}|
```python
def solution(id_list, report, k):
  answer = [0 for i in range(len(id_list))]
  reported = {x : 0 for x in id_list}

  report = set(report)

  for r in report:
      reported[r.split()[1]] += 1

  for r in report:
      if reported[r.split()[1]] >= k:
          answer[id_list.index(r.split()[0])] += 1

  return answer
```
