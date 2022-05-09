# WIL : Week 6
6주차에 대한 WIL

# kakao_60058 : 괄호 변환
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/60058
## 😎 Solved Code

### 💻 Code

```python
left = '('
right = ')'

def wrong_string(w):
    count = 0
    for i in range(len(w)):
        count += 1 if w[i] == left else -1
        if count < 0:
            return True
    return False

def process(w):
    if w == '':
        return w
    first_bracket = w[0]
    count = 1
    idx = 0
    for i in range(1, len(w)):
        count += 1 if w[i] == first_bracket else -1
        idx = i
        if count == 0:
            break
    u = w[:idx+1]
    v = w[idx+1:]
    if not wrong_string(u):
        return u + process(v)
    else:
        tmp = left + process(v) + right
        for i in u[1:-1]:
            tmp += left if i == right else right
        return tmp

def solution(p):
    return process(p)
```

### ❗️ 결과

성공

### 💡 접근

문제의 조건대로 차근차근 구현했다.

step2에서 `균형잡힌 괄호 문자열` 인 u를 구하기 위해 문자열 w를 순회하며 w[0]과 같은 문자가 나오면 count++, 아니면 count—를 했다. count가 0이 되면 좌,우 괄호의 개수가 동일하다는 뜻으로 break 한다.

`올바른 괄호 문자열` 을 확인하기 위해서도 유사한 방법을 구현했다. ‘(’가 나오면 count++, ‘)’가 나오면 count—를 하는데, count가 음수가 되는 순간 이는 올바른 괄호 문자열이 아니다.

## 🥳 문제 회고

구현 과정을 친절하게 명시해주어서 어렵지 않게 해결했다.

# kakao_60063 : 블록 이동하기
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/60063
## 😎 Solved Code

### 💻 Code

```python
from collections import deque

def out_of_range(y,x,N):
    return y < 0 or y >= N or x < 0 or x >= N

def move_or_rotate(y1,x1,y2,x2,board,N):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    res = []
    for i in range(4):
        ny1 = y1 + dy[i]
        nx1 = x1 + dx[i]
        ny2 = y2 + dy[i]
        nx2 = x2 + dx[i]
        if not out_of_range(ny1,nx1,N) and not out_of_range(ny2,nx2,N):
            if board[ny1][nx1] == 0 and board[ny2][nx2] == 0:
                res.append(((ny1,nx1),(ny2,nx2)))
    
    # 가로 -> 세로로 회전
    if y1 == y2:
        # 위로 회전
        if not out_of_range(y1-1,x1,N):
            if board[y1-1][x1] == 0 and board[y2-1][x2] == 0:
                res.append(((y1,x1),(y1-1,x1)))
                res.append(((y2,x2),(y2-1,x2)))
        # 아래로 회전
        if not out_of_range(y1+1,x1,N):
            if board[y1+1][x1] == 0 and board[y2+1][x2] == 0:
                res.append(((y1,x1),(y1+1,x1)))
                res.append(((y2,x2),(y2+1,x2)))
    else: # 세로 -> 가로로 회전
        # 왼쪽으로 회전
        if not out_of_range(y1,x1-1,N):
            if board[y1][x1-1] == 0 and board[y2][x2-1] == 0:
                res.append(((y1,x1),(y1,x1-1)))
                res.append(((y2,x2),(y2,x2-1)))
        # 오른쪽으로 회전
        if not out_of_range(y1,x1+1,N):
            if board[y1][x1+1] == 0 and board[y2][x2+1] == 0:
                res.append(((y1,x1),(y1,x1+1)))
                res.append(((y2,x2),(y2,x2+1)))
    return res

def solution(board):
    INF = int(1e10)
    N = len(board)
    answer = INF
    visited = []
    visited.append({(0,0),(0,1)})
    q = deque()
    q.append([{(0,0),(0,1)},0])

    while q:
        robot, count = q.popleft()
        robot = list(robot)
        y1, x1, y2, x2 = robot[0][0], robot[0][1], robot[1][0], robot[1][1]
        for n1,n2 in move_or_rotate(y1,x1,y2,x2,board,N):
            ny1,nx1 = n1[0], n1[1]
            ny2,nx2 = n2[0], n2[1]
            if not {(ny1,nx1),(ny2,nx2)} in visited:
                q.append([{(ny1,nx1),(ny2,nx2)},count+1])
                visited.append({(ny1,nx1),(ny2,nx2)})
                if (ny1 == N-1 and nx1 == N-1) or (ny2 == N-1 and nx2 == N-1):
                    answer = min(answer, count+1)
    return answer
```

### ❗️ 결과

성공

### 💡 접근

목적지까지 최단거리를 구하는 문제이므로 BFS로 접근했다.

다른 문제들과 다르게 좌표를 두 개씩 저장해야하므로 set() 자료형으로 이를 queue에 넣어준다.

또한 visited에 대한 정보를 단순 2차원 리스트에 좌표 형태로 기록할경우 정보의 손실이 발생할 수 있는 경우가 존재한다. 따라서 visited라는 1차원 리스트에 두 좌표를 묶은 set을 append 하는 식으로 방문정보를 기록한다.

나머지는 일반적인 BFS 문제와 유사하게 접근했으나, 문제의 회전조건 처리에 생각보다 코드가 길어졌다.

따라서 로봇이 이동할 수 있는 모든 경우의 좌표 리스트를 move_or_rotate 메소드에서 리턴하여 메인 함수에서 처리했다.

회전 처리시에 가로에서 회전할 경우, 세로에서 회전할 경우로 나눴다.

## 🥳 문제 회고

생각보다 엄청 삽질한 문제였다ㅠㅠ 처음에는 회전을 너무 어렵게 구현했다.... 채점 결과 분명 맞는거같은데 몇개가 에러가 나서 구글링을 했다. 회전 가능 조건 검사와 회전 구현이 생각보다 간단하다는 걸 알게되고 그대로 코드에 옮겼더니 성공했다. 중간고사 지나서 감 다 떨어진거같은데 얼른 복구 해야겠다!!!!

# kakao_60060 : 가사 검색
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/60060
## 🥺 Unsolved Code

### 💻 Code

```python
def solution(words, queries):
    answer = []
    words_dict = {}
    for i in range(100001):
        words_dict[i] = [] 
    for word in words:
        words_dict[len(word)].append(word)
    for query in queries:
        count = 0
        for word in words_dict[len(query)]:
            for i in range(len(query)):
                if query[i] == '?':
                    continue
                elif query[i] != word[i]:
                    break
            else:
                count += 1
        answer.append(count)      
    return answer
```

### ❗️ 결과

효율성 테스트 실패

### 💡 접근

단어 길이별로 딕셔너리에 word를 리스트로 저장한 뒤, query에 대해 길이가 같은 단어 리스트에서 하나씩 순회하며 검색.

### 🧐 접근에 대한 회고

효율성 테스트는 실패할 것을 알고 있었다. 시간복잡도는 O(query * word)로 10만 * 10만이다. 나름 인사이트를 얻을려고 쉬운 방법으로 먼저 풀었는데 진짜 도저히 생각이 안났다..

## 😎 Solved Code

### 💻 Code

```python
from bisect import bisect_left, bisect_right

def count_by_range(L, start, end):
    return bisect_right(L, end) - bisect_left(L, start)

def solution(words, queries):
    answer = []
    words_dict = {}
    words_dict_rev = {}
    for i in range(100001):
        words_dict[i] = [] 
        words_dict_rev[i] = []
    for word in words:
        words_dict[len(word)].append(word)
        words_dict_rev[len(word)].append(word[::-1])
        
    # 정렬
    for w in words_dict.values():
        w.sort()
    for w in words_dict_rev.values():
        w.sort()
    
    # 이진탐색
    for query in queries:
        if query[0] == '?':
            L = words_dict_rev[len(query)]
            start, end = query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')
        else:
            L = words_dict[len(query)]
            start, end = query.replace('?', 'a'), query.replace('?', 'z')
        answer.append(count_by_range(L, start, end))    
    return answer
```

### ❗️ 결과

성공

### 💡 접근

words_dict에 길이별로 저장.

words_dict_rev에 단어를 뒤집어서 길이별로 저장.

그 dict에 길이에 따라 저장된 단어들을 모두 정렬한다.

이제 query에 대해 매치된 단어의 개수를 세어주는데, 이진탐색을 이용한다.

query의 ?를 a로 치환한 값부터, query의 ?를 z로 치환한 값 사이에 있는 단어들의 개수를 세어주면 된다.

만약 query의 접두사에 ?가 온다면 뒤집은 query문을 치환한 뒤 words_dict_rev에서 탐색한다.

## 🥳 문제 회고

결국 구글에서 고수들의 아이디어를 빌렸다... 다른 풀이는 Trie 자료구조를 사용했는데 이진탐색으로 시간복잡도를 줄일 수 있다는 개념을 생각하면 쉽게 해결할 수 있다. bisect는 count_by_range 메소드는 다른 카카오 공채 문제에서도 다뤘던 메소드인데 다시 사용되는걸 보니 잘 익혀둬야겠다.

탐색의 대상이 숫자가 아닌 문자열이라 이진탐색을 써야한다는 생각과, 탐색의 시작과 끝 범위를 a와 z가 들어간 문자열로 치환하는 과정을 떠올리기 어려웠던 것 같다.