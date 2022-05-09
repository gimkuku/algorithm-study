# 카드_짝_맞추기.py


이 문제는 정말 제가 풀어본 구현중에서 제일 어려웠던 문제같았어요......

일단 저는 처음에 bfs로 거리 계산 안하고.. 가로 세로만 갈수있게 계산했는데, 계속 60점 나와서

라면 먹으면서 생각해보니깐 지그재그로 갈 수 있더라고요.. 바로 젓가락 내려놓고 풀었어요 라면은 불고..

마지막에 어떤 케이스를 생각 못했는데 뭐냐면

```python
for i in range(y+1, 4):
    if board[i][x] > 0 or i == 3:
        q.append([i, x])
        dist[i][x] = 1
        break

for i in range(y-1, -1, -1):
    if board[i][x] > 0 or i == 0:
        q.append([i, x])
        dist[i][x] = 1
        break
    
for j in range(x+1, 4):
    if board[y][j] > 0 or j == 3:
        q.append([y, j])
        dist[y][j] = 1
        break
    
for j in range(x-1, -1, -1):
    if board[y][j] > 0 or j == 0:
        q.append([y, j])
        dist[y][j] = 1
        break

```

이렇게 큐가 돌기 전에 카드들 위치를 전부 큐에 넣어주었어요

제가 잘못한건.. 이 dist[y][x] 값들을 바꿔놓아서

```python
for i in range(cy+1, 4):
    if board[i][cx] > 0 and dist[i][cx] != INF:
        break
    if (board[i][cx] > 0 or i == 3) and dist[i][cx] == INF:
        q.append([i, cx])
        dist[i][cx] = val + 1
        break
```

저 첫번째 if문이 없으면, 큐에 이상하게 들어가요

[1, 2, 1, 2] 이런 식의 값이 있고 [0, 0] 에서 시작할 때, [0, 2] 까지의 거리는 2여야 되는데

1로 계산되어서 틀렸더라고요.. 이거 어떻게 깔끔하게 못하나 ㅠㅠ dist 배열에다가 또 visited 배열까지 써야할까요..?

아무튼 그래서 이거 찾느라 30분 헤메고 결국 풀었습니다..


# 외벽_점검.py

`upper bound`, `lower bound`에 대한 개념을 다시 한번 제대로 상기할 수 있는 좋은 문제였습니다 ㅠㅠ 갓카오 역시 최고

아래는 틀린 코드입니다.

```python

import bisect as bs

def solution(n, weak, dist):
    wsize = len(weak)
    dsize = len(dist)
    
    visited = [False for _ in range(wsize)]
    
    def dfs(sidx, widx):
        # start is weak point value
        
        # end point
        if sidx <= widx:
            if visited[(sidx-1) % wsize]:
                return 0
        
        is_finish = True 
        for v in visited:
            if not v:
                is_finish = False
        
        if is_finish:
            return 0
        
        ret = float('inf')
        
        for i in range(sidx, widx+1):
            if i >= n:
                i = i % n
            visited[i] = True
        
        curr = weak[widx]
        
        for d in dist:
            next_widx = bs.bisect_right(weak, (curr+d) % n)
            if not visited[next_widx-1]:
                ret = min(ret, dfs(sidx, next_widx-1) + 1)
                
        for i in range(sidx, widx+1):
            if i >= n:
                i = i % n
            visited[i] = False 
        
        return ret
        
    ans = float('inf')
    
    # start everywhere
    for i in range(wsize):
        visited[i] = True
        ans = min(ans, dfs(i, i))
        visited[i] = False
        
    if ans == float('inf'):
        return -1
    return ans 
```

모듈러 써놓고 upper bound 사용한 제가 바보입니다... 디버깅 해보니깐 안되는 이유 바로 알고 배열을 바꿔봄

일단 제가 좋아하는 dfs를 이용했어요

시작점은 모든 곳이 될 수 있꼬 친구들도 아무나 데려올 수 있으므로 둘 다 visited 배열을 이용해서 중복방문이 되지 않게 만들어주는게 핵심인 것 같아요

각 노드에서는 다음 인덱스 위치를 upper bound를 이용해 계산을 해보는데 upper bound 이므로, 배열의 최대 인덱스보다 1 더 큰 인덱스가 나올 수 있습니다.

이 경우엔 다음 인덱스가 나타내는 '값'이 배열의 최대값보다 크다는 것이므로, 전체를 커버한다는 것을 알 수 있습니다.

그러므로 1을 리턴하는 것으로 예외처리를 해주었습니다.

만약 제 현재 위치가 시작보다 한바퀴 이상의 위치라면? 전부 돌았다는 것이므로 이 때 0을 리턴하여 값을 슉슉 받도록 해줬습니다.

이거 예외처리 하는데에서 갑자기 집중력 떨어져서 맞왜틀 쇼 좀 한거같아요


```python
if weak[widx] > weak[sidx+wsize-1]:
        #print(f"{weak[sidx]} START // {weak[widx]} END ?? {weak[sidx+wsize-1]}")
        return 0
    
    if left == 0:
        return float('inf')

```

문제의 예외처리 부분.. 자세하게 써보자면 

weak[widx]가 현재의 값이고 weak[sidx+wsize-1]이 딱 한바퀴를 도는 값입니다.

예를들어 n = 12, [1, 10, 11] 이라면 배열이 동그라니깐 [1, 10, 11, 13, 22, 23] 이 되고,

start를 1에서 시작했다면 sidx = 0, 1~11까지 전부 색칠되면 되는거죠? 

wsize = 3 (초기)

sidx+wsize-1 = 0+3-1 = 2

weak[sidx+wsize-1] = 11 입니다.

노드에 도착했다고 해서 색칠이 되는건 아니죠?? 더 커야 합니다..

어차피 앞에서 제일 큰 수보다 클 때를 예외처리 해주었기 때문에 값1로 시작했다면 13일때 11까지 칠해졌다는 것을 의미하므로

이 때 0을 리턴해주는 방식으로 풀었습니다..

말로 하니깐 좀 이상하네요 ㅎㅎ;;;


# 방금_그곡.py

샾 붙은거 잘 처리하면 잘 풀리는거 같아요..
