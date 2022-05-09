# WIL : Week 5
5주차에 대한 WIL
## for-else 구문
다음 두 코드는 동일한 결과를 출력한다.
```python
# 1번 코드
l = [1,5,3,2,7]
flag = True
for x in l:
  if x == 2:
    flag = False
    break

if flag:
  print ('2가 없다')

# 2번 코드
l = [1,5,3,2,7]
for x in l:
  if x == 2:
    break
else:
  print ('2가 없다')
```

가끔 for문을 사용하다보면 flag를 사용할 일이 있다. flag없이 for-else 구문을 사용하면 코드가 간결해진다.
for문이 break 없이 끝까지 순회를 마치면 else로 넘어가는 구조다.

# kakao_72415 : 카드 짝 맞추기
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/72415
## 😎 Solved Code

### 💻 Code

```python
from collections import deque
from itertools import permutations, product
import copy

def out_of_range(y,x):
    return y < 0 or y >= 4 or x < 0 or x >= 4

def bfs(board, sy, sx, ey, ex):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    counts = [[-1]*4 for _ in range(4)]
    counts[sy][sx] = 0
    q = deque([(sy,sx)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            for press_ctrl in range(2):
                ny = y + dy[i]
                nx = x + dx[i]
                if press_ctrl: # 컨트롤 눌렀을 때
                    while True:
                        if out_of_range(ny,nx):
                            ny -= dy[i]
                            nx -= dx[i]
                            break
                        if board[ny][nx] > 0:
                            break
                        ny += dy[i]
                        nx += dx[i]
                    if counts[ny][nx] == -1:
                        q.append((ny,nx))
                        counts[ny][nx] = counts[y][x] + 1
                        if ny == ey and nx == ex: # 만약 (ey,ex)에 도달했으면 탈출
                            return counts[ny][nx]
                else: # 컨트롤 안눌렀을 때
                    if not out_of_range(ny,nx):
                        if counts[ny][nx] == -1:
                            q.append((ny,nx))
                            counts[ny][nx] = counts[y][x] + 1
                            if ny == ey and nx == ex: # 만약 (ey,ex)에 도달했으면 탈출
                                return counts[ny][nx]
    return counts[ey][ex]
def solution(board, r, c):
    answer = int(1e9)
    cards = [[],[],[],[],[],[],[]] # cards[i]에 i번 카드 두 개의 좌표 존재
    cards_nums = []
    for y in range(4):
        for x in range(4):
            if 1 <= board[y][x] <= 6:
                cards[board[y][x]].append((y,x))
                cards_nums.append(board[y][x])
    cards_nums = list(set(cards_nums)) # 존재하는 카드 숫자들
    saved_board = copy.deepcopy(board) # 보드 초기 상태
	   
		# 처리할 카드 순서
    for cards_perm in permutations(cards_nums, len(cards_nums)):
				# 두 개의 카드 중 0 또는 1번쨰 부터 처리
        for start_idx in product([0,1], repeat=len(cards_nums)):
            count = 0
            y = r
            x = c
            for i in range(len(cards_nums)):
                card_num = cards_perm[i]
                curr = start_idx[i] # 0 또는 1
                first_y, first_x = cards[card_num][curr]
                second_y, second_x = cards[card_num][(curr+1)%2]
                
                # 첫번째 카드 삭제
                count += bfs(board, y, x, first_y, first_x) + 1
                board[first_y][first_x] = 0
                if count > answer: # 만약 계산 중간이 최솟값보다 크면 break
                    break
                    
                # 두번째 카드 삭제
                count += bfs(board, first_y, first_x, second_y, second_x) + 1
                board[second_y][second_x] = 0
                if count > answer: # 만약 계산 중간이 최솟값보다 크면 break
                    break
                
                # 현재 위치 갱신
                y = second_y
                x = second_x
            answer = min(answer, count)
            # board 복구
            for y in range(4):
                for x in range(4):
                    board[y][x] = saved_board[y][x]
          
    return answer
```

### ❗️ 결과

매우 아슬아슬하게 성공 (테스트 22, 25 시간초과로 고생했다...)

![스크린샷 2022-04-05 오후 11 25 55](https://user-images.githubusercontent.com/48646015/161786152-d233543a-f792-4d19-897a-3b59f48d4d0b.png)

### 💡 접근

현재 게임보드에서 (y1,x1)에서 (y2,x2)까지 도달하는 최소 조작 횟수를 알려주는 함수 Funct이 있다고 하자.

그럼 1~N 까지의 카드들에 대해 처리할 수 있는 모든 순서를 고려하여, Func를 적절히 호출하면 정답을 구할 수 있을것이다.

완전 탐색을 위해 고려한 사항들이다.

- 처리할 카드 순서 ( n종류의 카드에 대해 n! 가지)
- 카드 종류마다 두 개가 있는데, 어떤 것을 먼저 처리할지 (2^n 가지)

위의 두 가지를 고려하면 6가지 카드 순서를 다음과 같이 나타낼 수 있다.

- (첫번째 1)(두번째 1), (첫번째 2)(두번째 2), (첫번째 3)(두번째 3)...(첫번째 6)(두번째 6)
- (두번째 1)(첫번째 1), (첫번째 2)(두번째 2), (첫번쨰 3)(두번째 3)...(첫번째 6)(두번째 6)
- ...
- (두번째 6)(첫번쨰 6), (두번째 5)(첫번째 5),(두번째 4)(첫번째 4)...(두번째 1)(첫번째 1)

각각의 경우마다 조작횟수를 구해 최솟값을 도출하면 될 것이다.

여기까지 시간복잡도는 O(N!*2^N) = 46080 이다. (최대 N = 6)

그럼 (y1,x1)에서 (y2,x2)까지 도달하는 최소 조작 횟수를 알려주는 함수 Funct는 어떻게 구현할까.

BFS로 이를 구할 수 있다. 방문노드에 대해 상하좌우 한 칸, ctrl+상하좌우 로 최대 8가지 가지로 다른 노드로 방문할 수 있다.

일단 여기까지 해서 테스트 케이스 정답은 맞았다. 그런데 제출시 케이스 몇개가 시간초과가 떴다.

그래서 완전탐색에서 필요없는 탐색을 줄이고자 일종의 브레이크를 설정했다.

- BFS 내부에서 (y2,x2)에 도달하면 break (기존에는 queue가 빌 때까지 모두 탐색했다)
- BFS를 반복 호출하며 조작 횟수 계산를 count에 넣는데, 도중에 count가 최솟값 보다 커지면 탐색할 필요가 없으므로 break

이렇게 아슬아슬하게 시간 초과를 피해갔다...

## 🥳 문제 회고

처음에 DFS로 잘못 접근해서 꼬인 문제. 시간복잡도가 조금 꺼림칙하긴 했는데 완전탐색 + BFS 말고는 어떻게 풀지 도저히 상상히 안된다... 다른 풀이들도 많이 봐야겠다.

아마 실전이였으면 경우의 수를 줄일 브레이크를 고려하지 못해서 틀렸을 것 같다ㅠ

그리고 테스트 22, 25가 거의 10초가 걸렸기 떄문에 사실상 잘못된 풀이일수도 있다.

# kakao_60062 : 외벽 점검
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/60062
## 🥺 Unsolved Code

### 💻 Code

```python
def fix_weak(weak, d, n):
    MAX_COUNT = 1
    fix_weaks = []
    for w in weak:
        count = 0
        if d >= n:
            d = n-1
        end = w + d
        weaks = []
        for i in range(w,end+1):
            if i in weak:
                count += 1
                weaks.append(i)
        if end >= n:
            for i in range(0,(end+1)%n):
                if i in weak:
                    count += 1
                    weaks.append(i)
        if count > MAX_COUNT:
            fix_weaks = [weaks]
            MAX_COUNT = count
        elif count == MAX_COUNT:
            fix_weaks.append(weaks)
    return fix_weaks

def find(n, weak, dist, i):
    global MIN_NUM
    if i == len(dist):
        return
    fix_list = fix_weak(weak, dist[i], n)
    for fix in fix_list:
        remain_weaks = list(set(weak) - set(fix))
        remain_weaks.sort()
        if not remain_weaks:
            MIN_NUM = min(MIN_NUM, i+1)
        else:
            find(n, remain_weaks, dist, i+1)

def solution(n, weak, dist):
    answer = 0
    global MIN_NUM
    MIN_NUM = int(1e9)
    dist.sort(reverse=True)
    find(n, weak[:], dist, 0)
    return MIN_NUM if not MIN_NUM == int(1e9) else -1
```

### ❗️ 결과

일부 실패

### 💡 접근

그리디 알고리즘의 접근법을 떠올렸다.

dist를 내림차순 정렬한 뒤, 앞에서부터 꺼내서 취약부분을 고친다.

가장 긴 거리를 이동할 수 있는 친구를 먼저 이용하는 것이 가장 적은 수의 친구를 쓸 수 있다고 생각했다.

취약지점이 k개가 있다면, k개를 시작으로 점검하는 모든 경우의 수를 고려해야 할 것이다.

이 부분에서 find라는 함수로 재귀호출을 했다.

fix_weak에서 현재 남아있는 취약지점과 거리 d를 이동할 수 있는 친구에 대해 최대한 많은 지점을 고치고 남은 취약지점들을 리턴한다. 

### 🧐 접근에 대한 회고

사실 왜 틀렸는지 모르겠다... 가능한 모든 경우의수를 다 고려했다고 생각했다. 그리고 채점시 테스트 2개만 틀렸기 떄문에 약간의 예외가 있나 싶었다. 그런데 찾기가 너무 어려워서 포기하고 구글링을 했다.

## 😎 Solved Code

### 💻 Code

```python
from itertools import permutations

def count_friend(dist, weak, n):
    global MIN_NUM
    for i in range(len(weak)):
        new_weak = weak[i:]
        tmp = []
        for j in weak[:i]:
            tmp.append(j+n)
        new_weak += tmp
        count = 1
        cover_range = new_weak[0] + dist[0]
        for w in new_weak[1:]:
            if w <= cover_range:
                continue
            else:
                if count == len(dist):
                    count = int(1e9)
                    break
                cover_range = w + dist[count]
                count += 1
        MIN_NUM = min(MIN_NUM, count)
def solution(n, weak, dist):
    answer = 0
    global MIN_NUM
    MIN_NUM = int(1e9)
    for i in range(1,len(dist)+1):
        for d in permutations(dist, i):
            count_friend(d, weak, n)
    return MIN_NUM if MIN_NUM != int(1e9) else -1
```

### ❗️ 결과

성공

### 💡 접근

그리디 알고리즘 접근법을 포기하고 완전탐색으로 갔다.

완전탐색으로 모든 경우의 수를 다 고려한다. 고려할 모든 경우의수를 이루는 조건은 다음과 같다.

- 어느 지점에서 시작하는지 (ex. [1,2,3], [2,3,13], [3,13,14] n이 12일 때)
- 어떤 친구들을 보낼 것인지 (ex. [1],[2],[3],[1,2],[1,3],[2,3],[2,1]... 조합이 아닌 모든 순열!)

count_friend에서 모든 경우의 수에 대해 계산하여 MIN_NUM을 업데이트 해준다.

## 🥳 문제 회고

쉬운줄 알았는데 고민이 꼬리에 꼬리를 물다보니 많이 오래걸렸다...

구현 유형은 정말 모든 경우의수를 다 고려해서 풀 수 있는지 1차적으로 고민해야하는 것 같다.

# kakao_17683 : 방금그곡
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17683

## 😎 Solved Code

### 💻 Code

```python
def get_play_time(start, end):
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    return (eh-sh)*60 + (em-sm)

def get_song_list(song):
    song_list = []
    for s in song:
        if s == '#': # #이 있으면 마지막 원소에 덧붙임
            song_list[len(song_list) - 1] += '#'
        else:
            song_list.append(s)
    return song_list

def solution(m, musicinfos):
    answer = ''
    searched = []
    
    for info in musicinfos:
        start, end, title, song = info.split(",")
        play_time = get_play_time(start,end)
        
        song_list = get_song_list(song)
        m_list = get_song_list(m)

        song_len = len(song_list)
        m_len = len(m_list)
        
        played_song = [] # 실제로 재생된 음들
        for _ in range(play_time//song_len):
            played_song += song_list
        for i in song_list[:play_time%song_len]:
            played_song.append(i)
        
        for i in range(play_time - m_len + 1):
            for j in range(m_len):
                if played_song[i+j] != m_list[j]: # 다른게 있다면 break
                    break
            else: # 음이 모두 같았다면 searched에 append (for-else 구문)
                searched.append((play_time, title))
    
    max_play_time = 0
    for p, t in searched: # 최대 재생 시간 찾기
        if p > max_play_time:
            max_play_time = p
    
    for p, t in searched: # 최대 재생 시간 중 첫번째 곡
        if max_play_time == p:
            answer = t
            break
    return answer if answer != '' else "(None)"
```

### ❗️ 결과

성공

### 💡 접근

musicinfos를 순회하며 다음을 한다.

- 재생시간(분)을 계산한다
- 악보 정보에서 음들을 뽑아 song_list에 담는다
- 재생시간과 song_list를 고려해 실제 재생된 음들을 played_song에 넣는다
- m과 played_song을 비교하여 일치하면 searched에 넣는다

searched에서 최대 재생시간 곡중 첫번째 곡을 정답으로 return 한다

## 🥳 문제 회고

조금 번거로웠던 구현문제.

특히 악보를 스트링으로 저장하려다가 #때문에 리스트로 바꿨다.

처음으로 for-else 구문을 사용해서 문제를 풀었는데 flag가 필요하지 않아 깔끔했다.