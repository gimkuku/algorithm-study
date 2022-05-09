# 1. 사라지는 발판
## 참고
https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

정답률이 0.78%...
게임판의 크기가 크지 않고, 발판을 밟으면 사라진다는 조건이 있어 탐색해야하는 가짓수가 크게 감소하므로 `완전탐색`으로 해결할 수 있는 문제이다.
`input`으로 게임판의 상태, A, B의 위치를 받아 이번 턴에 움직여야하는 플레이어의 승패 여부, 총 이동 횟수를 `return`하는 재귀함수를 이용한 완전탐색으로 해결하면 된다.

## 풀이
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|board|게임 보드의 초기 상태를 나타내는 2차원 정수 배열|[[1, 1, 1], [1, 1, 1], [1, 1, 1]]|
|aloc, bloc|각 A, B의 캐릭터 초기 위치를 나타내는 정수 배열|[1, 0]|

### 📁 필요한 함수들
1. **A의 승패 여부와 플레이어의 총 이동 횟수를 반환하는 함수 (A함수)**<br /><br />
    A가 상하좌우 4가지 방향 중 이동할 수 있는 방향으로 이동하여 게임판의 상태를 바꾼 뒤, 그 상태를 B에게 넘기는 방식으로 동작(B함수 호출)
    함수 입출력 설명
    |이름|설명|예시|
    |------|---|---|
    |board|`입력` 현재 보드의 상태|[[1, 1, 1], [1, 1, 1], [1, 1, 1]]|
    |aloc, bloc|`입력` 각 현재 A,B의 위치|[1, 0]|
    |total_move|`입력` 지금까지의 총 이동 횟수|5|
    |result|`리턴` [ A의 승리 가능성 여부 , A의 승리 가능성이 있는 경우 총 이동 횟수 중 최솟값 or A의 승리 가능성이 없는 경우 총 이동 횟수 중 최댓값 ]|[True, 5]|
    ```python
    def A_func(board,aloc,bloc,total_move):
      a_x,a_y = aloc

      # A의 현재 위치의 발판이 없는 경우, [패배, 전 턴까지의 총 이동 횟수] 반환
      if board[a_x][a_y] == 0:
          result = [False,total_move]
          return result

      cango = False # A가 상하좌우 중 이동할 수 있는 곳이 있는 경우 True로 전환
      canwin = [] #  A가 이길 수 있는 경우들의 총 이동횟수들을 담은 값
      nowin = [] # A가 질 수 밖에 없는 경우들의 총 이동횟수들을 담은 값

      # 상하좌우 방향으로 이동하기 위한 변수와 반복문
      dx = [-1,1,0,0]
      dy = [0,0,-1,1]
      for i in range(4):
          next_x = a_x + dx[i]
          next_y = a_y + dy[i]
          
          # 이동할 수 있는 경우
          if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
              if board[next_x][next_y] == 1:
                  next_board = copy.deepcopy(board)
                  next_board[a_x][a_y] = 0
                  # B이동을 위한 B함수 호출
                  b_win,cnt_move = B_func(next_board,(next_x,next_y),bloc,total_move+1)
                  # B가 이길 가능성이 없는 경우, canwin 배열에 지금까지 총 이동횟수 추가
                  if b_win == False:
                      canwin.append(cnt_move)
                  # B가 이길 가능성이 있는 경우, nowin 배열에 지금까지 총 이동횟수 추가
                  else:
                      nowin.append(cnt_move)
                  cango = True
      
      # 이동한 경우
      if cango:
          # 승리 가능성이 있는 경우, [승리, canwin 배열 원소들 중 최솟값] 반환
          if canwin:
              result = [True, min(canwin)]
          # 승리 가능성이 없는 경우, [패배, nowin 배열 원소들  최댓값] 반환
          else:
              result = [False,max(nowin)]
              
      # 이동하지 못한 경우, [패배, 전 턴까지의 총 이동 횟수] 반환
      else:
          result = [False,total_move]

      return result
    ```
    <br />
2. **B의 승패 여부와 플레이어의 총 이동 횟수를 반환하는 함수 (B함수)**<br /><br />
    A함수와 같은 원리

    ```python
    def B_func(board,aloc,bloc,total_move):
      b_x,b_y = bloc

      if board[b_x][b_y] == 0:
          result = [False,total_move]
          return result

      cango = False
      canwin = []
      nowin = []

      dx = [-1,1,0,0]
      dy = [0,0,-1,1]

      for i in range(4):
          next_x = b_x + dx[i]
          next_y = b_y + dy[i]

          if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
              if board[next_x][next_y] == 1:
                  next_board = copy.deepcopy(board)
                  next_board[b_x][b_y] = 0
                  a_win,cnt_move = A_func(next_board,aloc,(next_x,next_y),total_move+1)
                  if a_win == False:
                      canwin.append(cnt_move)
                  else:
                      nowin.append(cnt_move)
                  cango = True

      if cango:
          if canwin:
              result = True,min(canwin)
          else:
              result = False,max(nowin)

      else:
          result = False,total_move

      return result
    ```

3. **솔루션 함수**<br />

    ```python
    def solution(board, aloc, bloc):
    return A_func(board,aloc,bloc,0)[1]
    ```
    
<br />

# 2. 행렬 테두리 회전하기

## 풀이
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|rows, columns|각 행렬의 세로 길이(행 개수), 가로 길이(열 개수)|6|
|queries|회전들의 목록, 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며 x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전|[[2,2,5,4],[3,3,6,6],[5,1,6,3]]|

### 📁 필요한 함수들
1. **주어진 크기에 해당하는 보드를 만드는 함수**<br /><br />
    함수 입출력 설명
    |이름|설명|예시|
    |------|---|---|
    |rows, columns|`입력` 보드의 세로 길이(행 개수), 가로 길이(열 개수)|6|
    |board|`리턴` 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있는 보드|[[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]|
    ```python
    def make_board(rows, columns):
      board = [[1 for col in range(columns)] for row in range(rows)]
      index = 0
      for row in range(rows):
          for col in range(columns):
              board[row][col] += index
              index += 1
      return board
    ```
    <br />
2. **각 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 담은 배열을 구하는 함수**<br /><br />
    함수 입출력 설명
    |이름|설명|예시|
    |------|---|---|
    |board|`입력` 현재 보드의 상태|[[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]|
    |queries|`입력` 회전들의 목록|[[2,2,5,4],[3,3,6,6],[5,1,6,3]]|
    |result|`리턴` queries의 각 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 담은 배열|[8, 10, 25]|

    ```python
    def get_mins(board, queries):
      result = []

      # 회전
      for x1,y1,x2,y2 in queries:
          # 각 행,열의 인덱스는 주어진 x1,y1,x2,y2보다 1씩 작으므로 빼준다
          x1 -= 1
          y1 -= 1 
          x2 -= 1
          y2 -= 1

          # 시작 숫자를 저장해놓는다
          start = board[x1][y1]
          _min = [start]

          # (y1열) x2행 -> x1행 방향 회전
          for i in range(x1,x2,1):
              temp = board[i+1][y1]
              board[i][y1] = temp
              _min.append(temp)

          # (x2행) y2열 -> y1열 방향 회전
          for i in range(y1,y2,1):
              temp = board[x2][i+1]
              board[x2][i] = temp
              _min.append(temp)

          # (y2열) x1행 -> x2행 방향 회전
          for i in range(x2,x1,-1):
              temp = board[i-1][y2]
              board[i][y2] = temp
              _min.append(temp)

          # (x1행) y1열 -> y2열 방향 회전
          for i in range(y2,y1,-1):
              temp = board[x1][i-1]
              board[x1][i] = temp
              _min.append(temp)

          # 시작 숫자가 시계방향으로 이동한 위치에 저장해놓았던 시작 숫자를 담는다
          board[x1][y1+1] = start
          result.append(min(_min))

      return result
    ```

3. **솔루션 함수**<br />

    ```python
    def solution(rows, columns, queries):
      board = make_board(rows, columns)

      return get_mins(board, queries)
    ```
    
<br />

# 3. 다단계 칫솔 판매

## 풀이
### 📁 주어진 입력 및 예시 이해
|이름|설명|예시|
|------|---|---|
|enroll|각 판매원의 이름을 담은 배열|['john', 'mary', 'edward', 'sam', 'emily', 'jaimie', 'tod', 'young']|
|referral|각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열|['-', '-', 'mary', 'edward', 'mary', 'mary', 'jaimie', 'edward']|
|seller|판매량 집계 데이터의 판매원 이름을 나열한 배열|['young', 'john', 'tod', 'emily', 'mary']|
|amount|판매량 집계 데이터의 판매 수량을 나열한 배열|[12, 4, 2, 5, 10]|

### 📁 솔루션 함수
함수 내 변수 설명
|이름|설명|예시|
|------|---|---|
|answer|각 판매원의 이름과 이 사람에게 배분된 이익금의 총합이 나열된 딕셔너리|{'john': 360, 'mary': 958, 'edward': 108, 'sam': 0, 'emily': 450, 'jaimie': 18, 'tod': 180, 'young': 1080}|
|parent|각 판매원의 이름과 이 사람을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 딕셔너리|{'-': '-', 'john': '-', 'mary': '-', 'edward': 'mary', 'sam': 'edward', 'emily': 'mary', 'jaimie': 'mary', 'tod': 'jaimie', 'young': 'edward'}|

저번주 코드리뷰를 하며 새로 알게된 딕셔너리에서 value 값만 추출해 반환하는 법을 사용했다. 코드리뷰가 정말 큰 도움이 되는구나라는 생각..! 
- 참고 : https://github.com/gimkuku/algorithm-study/blob/master/code/S-J-Kim/week2/kakao_92334.py 중 `return list(mail_count.values())` 부분

```python
import math

def solution(enroll, referral, seller, amount):
    answer = {name: 0 for name in enroll}
    parent = {'-':'-'}

    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]

    for i in range(len(seller)):
        people = seller[i]
        profit = amount[i]*100
        while people != "-" and profit >= 1:
            answer[people] += math.ceil(profit*0.9)
            profit -= math.ceil(profit*0.9)
            people = parent[people]

    return list(answer.values())
```
<br />
