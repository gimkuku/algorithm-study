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

## 외벽점검 (60062)
ㅇ아ㅏㅏㅏ너무 어려워요.. 


### 성공 해결 방법
여러 블로그들을 참조 - 주말에도 한번 더 봐야겠습ㄴ디ㅏ..
1. 방향 문제를 해결해주기 위해 배열을 더블링해서 높은 숫자의 포인트에서도 낮은 숫자 포인트로 이동할 수있게 ? 만든다
2. 친구들의 순서를 순열로 만들어서 각 포인트에서 시작했을때, 모든 것을 커버치는지 확인한다


..원형 배열도 어떻게 생각해내나 했는데 완전탐색도 코드가 쉽지가 않네요...



## 방금 그곡 (17683)
문제 제대로 안읽어서 가장 큰 재생 시간 

### 실패한 해결 방법
1. 처음에는 C#, C 이런것들을 하나의 요소로 만들어서 list화 했습니다
2. 그리고 substring을 예전에 DP로 풀었던 기억이 있어서 DP로 풀었습니다.
3. 일단 너무 복잡........ 한데 채점해보면 마지막 테케가 틀렸더군요... 아직까지 이유를 못찾았습니다. 

아래는 실패한 해결방법 (마지막 테케30번 하나만 틀렸는데 왜 틀리겠는지 못찾음 ㅠ)
```python

def full_music(minfo):
    st, et, t, music_part = minfo.split(',')
    
    music_part = parse_music(music_part)
    
    sh, sm = map(int, st.split(':'))
    eh, em = map(int, et.split(':'))
    
    play_time = (eh*60 + em) - (sh*60 + sm)
    
    if play_time < len(music_part):
        full_music = music_part[0:play_time]
    else:
        iter_time = play_time // (len(music_part))
        last_time = play_time % (len(music_part))
        print(iter_time)
        print(last_time)
        full_music = music_part*iter_time + music_part[0:last_time]
    print(full_music)
    return (t, play_time, music_part)


def parse_music(m_str):
    m_str = list(m_str.strip())
    
    result = []
    
    for i in range(len(m_str)):
        
        if m_str[i] == '#':
            n_str = m_str[i-1] + m_str[i]
            result.pop()
            result.append(n_str)
        else:
            result.append(m_str[i])
            
    return result
    
def is_same(m, music, play_time, title, answer_list):

    # dp[i][j] music의 i까지보고 m의 j까지 봤을 때의 일치하는지?
    dp = [[0] * len(music) for _ in range(len(m))]

    for i in range(len(m)):
            for j in range(len(music)):
                if m[i] == music[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] == len(m):
                        answer_list.append((play_time, title))
                        return
                        
                else:
                    dp[i][j] = 0

def solution(m, musicinfos):
    

    m = parse_music(m)
    print(m)
    
    answer_list = []
    answer_list_idx = 0
    for minfo in musicinfos:
        title, play_time, music = full_music(minfo)
        
        is_same(m, music, play_time, title, answer_list)
    
        
                    
    if len(answer_list) == 0:
        answer = '(None)'
    else:
        answer_list.sort(key = lambda x: -x[0])
        answer = answer_list[0][1]
    
    return answer
```


### 성공 해결 방법
1. DP로 풀다가 계속 위와 같은 코드로 마지막 테케만 틀려서 짜증나서 걍 python string의 in을 써야겠다고 생각했습니다.
2. string in을 사용하려면 위에 방법처럼 직접 음표로 치환하여 리스트화하면 안됐었습니다.
3. C# -> c 이렇게 소문자로 바꿔서 음을 바꾸어 준 후 python 의 in을 사용하여 풀었습니다.


