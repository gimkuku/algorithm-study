# WIL


## 카드 짝 맞추기 (72412)
개인적으로 의지를 꺾어버리는 문제였습니다..ㅎㅎ 
결국은 여러가지 블로그들을 참고하여 문제를 풀었습니다...!

### 실패한 해결 방법
1. 출발점 r, c에서 같은 짝을 찾아가는 BFS를 만들어보자는 생각을 가짐
2. 문제가 여러가지 생김 -> r, c 캐릭터 카드에서 시작해서 다음 같은 카드까지 가는데에가 최소? ---> 그렇다 하더라도 이러한 순서로 가는게 최종적으로 최소가 될까? / r,c가 캐릭터 카드가 아닌 빈 곳에서 시작할수도 있지 않을까? 
3. 너무 복잡........ 결국 모든 카드 순서의 경우의 수를 다봐야 하는데 시간 초과가 되지 않을까???
4. 블로그 보자

### 성공 해결 방법
여러 블로그들을 참조
- 카드들을 방문하는 순서를 순열로 해서 모든 경우를 구해야한다
    - 결국 카드들을 모두 소거하기 위해서는 규칙상, A type의 카드 1번을 방문했다면 바로 다음에는 A type의 카드 2번을 방문해야 한다
    - 카드는 총 16개인데 16개에 대해서 순열을 한다면 시간초과? -> 종류를 가지고 순열을 만든다면 8!이므로 괜찮다? 

- dictionary로 카드 분류하기

```python
def solution(board, r, c):
    global answer, adict, n_board
    
    # borad를 global로 사용하기 위해 deepcopy
    n_board = deepcopy(board)
    
    # board를 완전탐색하여 adict에 캐릭터 별로 분류
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in adict.keys():
                    adict[board[i][j]] = [(i, j)]
                else:
                    adict[board[i][j]].append((i, j))
                    
    character = list(adict.keys())
    orders = list(permutations(character, len(character)))
    
    
    for order in orders:
        back_tracking(r, c, order, 0, 0)
        
    
    return answer
```


- Back - Tracking
    - A type의 카드라도 카드1 -> 카드2 / 카드2 -> 카드1 로 방법이 두가지 있다
    - 만약 카드 종류가 세개라면 총 2*2*2의 8가지 방법의 경우가 있다
    - dfs와 back tracking을 통해 구현해준다

```python
def remove(character_idx):
    global n_board, adict
    for r, c in adict[character_idx]:
        n_board[r][c] = 0
        
def recover(character_idx):
    global n_board, adict
    for r, c in adict[character_idx]:
        n_board[r][c] = character_idx

                
def back_tracking(r, c, order, idx, cnt):
    global answer, adict
    # 목적 back tracking을 하면서 1A, 1B 순서 왔다 갔다 하기
    if idx == len(order):
        answer = min(answer, cnt)
        return
    
    c1r, c1c = adict[order[idx]][0][0], adict[order[idx]][0][1]
    c2r, c2c = adict[order[idx]][1][0], adict[order[idx]][1][1]
    
    #### 시작점 -> 같은 character 카드 1 -> 같은 같은 character 카드 2 ####
    cost1 = bfs(r, c, c1r, c1c) # 시작점에서 첫번째 타겟과의 cost
    cost2 = bfs(c1r, c1c, c2r, c2c) # 첫번째 타겟에서 두번째 타겟과의 cost
    
    remove(order[idx]) # character_idx 카드 없애기
    back_tracking(c2r, c2c, order, idx+1, cnt+cost1+cost2) # 같은 같은 character 카드 2 -> 다음 카드 묶음  dfs
    recover(order[idx]) # backtraking 후 다시 character_idx 살리기
    
    
    ### 시작점 -> 같은 character 카드 2 -> 같은 같은 character 카드 1 ###
    cost1 = bfs(r, c, c2r, c2c) # 시작점에서 두번째 타겟과의 cost
    cost2 = bfs(c2r, c2c, c1r, c1c) # 두번째 타겟에서 첫번째 타겟과의 cost
    
    remove(order[idx]) # character_idx 카드 없애기
    back_tracking(c1r, c1c, order, idx+1, cnt+cost1+cost2) # 같은 같은 character 카드 1 -> 다음 카드 묶음  dfs
    recover(order[idx]) # backtraking 후 다시 character_idx 살리기
    
```

- 한 카드에서 다른 카드로 가는 cost - BFS
    - 목적지가 같은 경우 Enter 키를 치는 횟수 고려하여 return
    - 초기 출발지와 목적지가 같은 경우 대해서 예외 처리 

```python
def bfs(sr, sc, dr, dc):
    global n_board
    visited = [[False] * 4 for _ in range(4)]
    
    # 만약 출발지와 목적지가 같은 경우
    if sr == dr and sc == dc:
        return 1 # Enter 1회만 counting
    
    q = deque()
    q.append((sr, sc, 0))
    visited[sr][sc] = True
    
    while q:
        cr, cc, cnt = q.popleft()
        
        for d in range(4):
            nr, nc = cr + dx[d], cc + dy[d]
            
            if 0<=nr<4 and 0<=nc<4:
                if visited[nr][nc] is False:
                    visited[nr][nc] = True
                    if nr == dr and nc == dc:
                        return cnt+2
                    else:
                        q.append((nr, nc, cnt+1))
                
                
            nr, nc = ctrl(d, cr, cc)
            
            if 0<=nr<4 and 0<=nc<4:
                if visited[nr][nc] is False:
                    visited[nr][nc] = True
                    if nr == dr and nc == dc:
                        return cnt+2
                    else:
                        q.append((nr, nc, cnt+1))
```