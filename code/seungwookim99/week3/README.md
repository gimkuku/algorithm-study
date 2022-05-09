# WIL : Week 3
3주차에 대한 WIL
## MiniMax 알고리즘
바둑과 체스 같은 1:1 대결에서 서로 최선의 플레이를 하는 방식이 MiniMax Algorithm이다.

최선의 플레이란 다음과 같다.
- 내 차례에 나는 내게 가장 큰 이득이 되는 플레이를 한다.
- 상대방은 내게 가장 손해가 되는 플레이를 한다.

예를 들어 A와 B가 1~32가 적힌 카드를 가지고 게임을 한다.

A와 B는 매 턴마다 카드의 절반을 없앨 수 있다. 

A는 남은 카드의 합이 최대가 되게끔 플레이를 하고, B는 최소가 되게끔 플레이를 한다.

A가 선공이라면 A는 1~16을 버릴 것이다 (A에게 가장 큰 이득 = B에게 가장 큰 손해)

B가 후공이라면 B는 25~32를 버릴 것이다 (B에게 가장 큰 이득 = A에게 가장 큰 손해)

위와 같은 논리 흐름이 MiniMax Algorithm이다. A가 바보같이 17~32를 버리는 플레이를 하진 않을 것이다.
이번 주차의 사라지는 발판 문제 상황과 일치하는 논리적 흐름이라고 이해할 수 있다. 어떻게 보면 `그리디 알고리즘`의 컨셉이
내재되어있다고 생각할 수 있을 것 같다.

자세한 내용은 Readme 하단에 링크를 걸어두었다.

## Dictionary의 operation 시간복잡도
리스트에서 O(N)에 할 수 있는 operation을 Dictionary에서 O(1)에 할 수 있다.
```python
L = ['a','b','c',...,'z']
D = {
  'a' : 0,
  'b' : 1,
  ...
  'z' : 25
}
```
여기에서 z의 인덱스를 구한다면 각각 다음과 같은 시간복잡도가 소요된다.
```python
L.index('z') # 0~N까지 순회 : O(N)
D['z'] # O(1)
```

자세한 내용은 다단계 칫솔 판매 문제 회고 하단에 링크를 걸어두었다.

# kakao_77485 : 행렬 테두리 회전하기
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/77485
## 😎 Solved Code
```python
def solution(rows, columns, queries):
    answer = []
    board = []
    # 행렬 초기화
    for row in range(rows):
        tmp = []
        for col in range(columns):
            tmp.append(row * columns + col + 1)
        board.append(tmp)
        
    for x1,y1,x2,y2 in queries:
        x1 -=1
        y1 -=1
        x2 -=1
        y2 -=1
        min_num = initial_value = board[x1][y1]
        # 좌측 테두리 갱신
        for i in range(x1,x2):
            board[i][y1] = board[i+1][y1]
            min_num = min(min_num, board[i][y1])
        # 하단 테두리 갱신
        for i in range(y1,y2):
            board[x2][i] = board[x2][i+1]
            min_num = min(min_num, board[x2][i])
        # 우측 테두리 갱신
        for i in range(x2,x1,-1):
            board[i][y2] = board[i-1][y2]
            min_num = min(min_num, board[i][y2])
        # 상단 테두리 갱신
        for i in range(y2,y1,-1):
            board[x1][i] = board[x1][i-1]
            min_num = min(min_num, board[x1][i])
        board[x1][y1+1] = initial_value
        answer.append(min_num)
    return answer
```
### ❗️ 결과
성공
### 💡 접근
- (x1,y1) 값을 초기값, 최소값으로 둔다.
- 매 query 마다 (x1,y1,x2,y2)에 대해 반시계 방향으로 순회하며 회전작업을 수행한다.
- 수행작업마다 최소값과 비교하며 최소값을 갱신한다.
- 순회를 마친 뒤 마지막에 `board[x1][y1+1] = 초기값`
## 🥳 77485 : 행렬 테두리 회전하기 문제 회고
row, col, query 길이 조건이 까다롭지 않았다. 그래서 그냥 단순하게 원소 하나하나를 순회하는 로직으로 구현했다.
시간복잡도는 O(queries * (rows + columns)) 이다.


# kakao_77486 : 다단계 칫솔 판매
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/77486
## 🥺 Unsolved Code
```python
def solution(enroll, referral, seller, amount):
    answer = [0] * (len(enroll))
    for i in range(len(seller)):
        profit = amount[i] * 100
        s = seller[i]
        while s != '-':
            if profit < 10:
                seller_idx = enroll.index(s)
                answer[seller_idx] += profit
                break
            else:
                commission = int(profit * 0.1)
                profit -= commission
            seller_idx = enroll.index(s)
            answer[seller_idx] += profit
            profit = commission
            s = referral[seller_idx]
    return answer
```
### ❗️ 결과
테스트 10,11,12,13 4개 시간초과로 실패
### 💡 접근
Union-Find가 생각났다. referral이 부모 노드에 대한 정보를 담고있기 때문에 현재 노드(판매원)에서 부터 부모 노드를 잘 타고 올라가면 쉽게 구현할 것 같았다.

- answer를 `[0]*enroll길이`로 초기화한다
- 주어진 seller 정보를 순회한다
- while문 안에서 부모 노드를 타고 올라가며 수익을 배분하는 작업을 한다
- 현재 노드 기준 profit이 10 이상이면, commission과 profit을 비율대로 나눈다
- `.index 메소드`로 현재 노드(판매원)의 인덱스를 알아내고, 그 인덱스로 부모 노드를 알아낸다
- 현재 판매원의 수익(answer) += profit 을 하고, profit = commission 으로 부모노드에게 수수료를 전달한다
- 현재 판매원(s)를 부모 노드로 갱신하고 다음 iteration으로 넘어간다
- 만약 현재 노드 기준 profit이 10보다 작으면, profit 전체를 현재 판매원이 가져가고 break 한다
- 만약 루트 노드(민호)에 도달하면 break 한다
### 🧐 접근에 대한 회고
무한루프 걸렸거나 시간복잡도로 인해 터졌나 싶었다.
근데 amount 원소 최대값이 100이므로 최대 수익이 10,000인데 이는 while문이 도는데 최대 5번 걸린다는 뜻이다. 왜냐하면 수수료를 위로 전달하는 과정이 10,000 -> 1,000 -> 100 -> 10 -> 1(break) 이기 때문이다. 그럼 시간복잡도는 O(seller)이므로 시간복잡도 문제는 아닌 듯 했다.

그런데 다시 코드를 보니까 `enroll.index(s)`를 보고 아차 싶었다. enroll을 순회하며 index를 찾기 위해 O(enroll)이 걸릴 것이기 때문에... 실제는 O(seller*enroll) = 10억이라 터진 것 같았다.

저 부분을 개선해야겠다.

## 😎 Solved Code
```python
def solution(enroll, referral, seller, amount):
    answer = [0] * (len(enroll))
    enroll_dict = {} # 판매원들의 인덱스를 미리 저장해둔 딕셔너리
    for i in range(len(enroll)):
        enroll_dict[enroll[i]] = i
    for i in range(len(seller)):
        profit = amount[i] * 100
        s = seller[i]
        while s != '-':
            if profit < 10:
                # seller_idx = enroll.index(s) <- O(n)으로 순회하는 부분 없애고
                seller_idx = enroll_dict[s] # 딕셔너리에서 인덱스 불러오기
                answer[seller_idx] += profit
                break
            else:
                commission = int(profit * 0.1)
                profit -= commission
            # seller_idx = enroll.index(s)
            seller_idx = enroll_dict[s] # 마찬가지로 딕셔너리에서 인덱스 불러오기
            answer[seller_idx] += profit
            profit = commission
            s = referral[seller_idx]
    return answer
```

### ❗️ 결과
성공
### 💡 접근
위의 방식과 접근은 동일하다. 하지만 .index이 O(N) 으로 예상되기 때문에 이를 O(1)에 해결하고자 했다.
이를 위해 enroll_dict라는 딕셔너리를 만들어 key = 판매원 이름, value = 인덱스 정보를 저장했다. 

## 🥳 77486 : 다단계 칫솔 판매 문제 회고
시키는 대로만 따라하면 되는 구현문제였던 것 같다. 대신 어떤 자료형을 써야하는지 함정이 있었던 것 같다.

문제를 풀면서 확인하게 된 사실은 Dictiory에 대해 `dict[key]` Operation은 O(1)의 시간복잡도가 걸린다는 것이다. 만약 key값들이 저장된 list에서 특정 key값의 index를 찾는다면 0번째 값부터 순회해야하므로 O(N)의 시간복잡도가 걸릴 것이다. 하지만, Dictonary를 이용해 key에 대응되는 value에 index를 넣어주면 O(1)에 해당 key의 index를 조회할 수 있다.

Ref : https://velog.io/@kimwoody/Python-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%99%80-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC%EC%9D%98-%EC%A3%BC%EC%9A%94-%EC%97%B0%EC%82%B0-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84




# kakao_92345 : 사라지는 발판
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/92345
## 🥺 Unsolved Code
```python
import copy

def is_a_winner(width, height, board, aloc, bloc, count):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    ay, ax = aloc
    by, bx = bloc
    
    # move a
    board_status = []
    A_status = []
    for i in range(4):
        newAy = ay + dy[i]
        newAx = ax + dx[i]
        if (0 <= newAx < width) and (0 <= newAy < height):
            if board[newAy][newAx]:
                tmp = copy.deepcopy(board)
                tmp[ay][ax] = 0
                tmp[newAy][newAx] = 1
                board_status.append(tmp)
                A_status.append([newAy,newAx])

    # a가 더이상 움직일 곳이 없으면
    if not board_status:
        return -1

    # move b
    candidate = []
    for i in range(len(board_status)):
        new_board = board_status[i]
        newAy, newAx = A_status[i]
        if new_board[by][bx] == 0: # a가 이동해서 b가 있던 발판이 사라진 경우
            candidate.append(count+1)
        else:
            max_count = -1
            can_b_move = False
            for i in range(4):
                newBy = by + dy[i]
                newBx = bx + dx[i]
                if (0 <= newBx < width) and (0 <= newBy < height):
                    if new_board[newBy][newBx]:
                        can_b_move = True
                        new_board[newBy][newBx] = 1
                        new_board[by][bx] = 0
                        max_count = max(max_count, is_a_winner(width, height, copy.deepcopy(new_board), [newAy,newAx], [newBy,newBx], count+2))
            if can_b_move:
                candidate.append(max_count)
            else:
                candidate.append(count+1)
        
        # a가 이동할 수 있는 경우의수 중 -1 또는 0 이상의 최솟값 return
        if -1 not in candidate:
            return min(candidate)
        else:
            min_num = candidate[0]
            for i in candidate:
                if i != -1 and i > min_num:
                    min_num = i
            return min_num

def solution(board, aloc, bloc):
    answer = -1
    width = len(board[0])
    height = len(board)
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    ay,ax = aloc
    # A 차례
    A = is_a_winner(width, height, copy.deepcopy(board), aloc, bloc, 0)

    # B 차례
    B = 99999
    for i in range(4):
        newAy = ay + dy[i]
        newAx = ax + dx[i]
        if (0 <= newAx < width) and (0 <= newAy < height):
            if board[newAy][newAx]:
                a_moved_board = copy.deepcopy(board)
                a_moved_board[ay][ax] = 0
                a_moved_board[newAy][newAx] = 1
                tmp = is_a_winner(width, height, a_moved_board, bloc, [newAy, newAx], 1)
                if tmp == -1:
                    B = -1
                    break
                else:
                    B = min(B, tmp)
    if A == -1 and B == 99999: # 초기 조건 그대로면 => a 패배
        return 0
    elif A == -1: # A가 지면
        return B
    elif B == -1 : # B가 지면
        return A
    else:
        return min(A,B)
```
### ❗️ 결과
일부 성공, 일부 실패
### 💡 접근
문제를 보니 board와 a,b 위치 정보만 주어지면 반드시 누가 이길지 판별할 수 있다고 한다. 테스트 케이스를 보며 다음과 같이 접근해보았다.

i번째 턴이 되었고 A가 이동할 차례라고 해보자. 그리고 다음과 같은 상황이다.
- A는 상,하,좌,우 중에서 상, 하 두 방향으로만 이동할 수 있다.
- A가 상으로 갈 경우 B는 세 방향으로 이동할 수 있고, A가 하로 갈 경우 B는 한 방향으로 이동할 수 있다.
- A는 현재 위치에서 반드시 승리할 수 있다.

A가 반드시 승리할 수 있다면 어떤 조건을 만족해야할까?
- i번째 턴에서 A가 상, 하 두 방향 중 반드시 하나 이상은 이기는 경우가 존재한다.
- A가 반드시 이기는 i번째 이동에 대해, i+1번째 B가 어떠한 방향을 가더라도 i+2번째에서 A가 이길 수 있는 경우가 존재한다.

예를 들어 i번째 = A가 상으로 이동 했다고 하면, B가 갈 수 있는 세 방향 중 어떤 방향을 가더라도, i+2번째 A가 이길 수 있는 경우가 존재한다.

여기까지 생각이 정리됐을 때 재귀호출로 완전탐색을 해야겠다고 생각했다. 그리고 위의 난잡한 코드는 이를 구현해보려고 한 것인데 실패했다.

다음은 위의 코드를 어떻게 구현했는지에 대한 설명이다.
- 우선 `is_a_winner` 메소드는 aloc에 위치한 플레이어가 이길 수 있다면 최소횟수를, 진다면 -1을 리턴한다.
- solution 메소드에서 A에 대해 `is_a_winner`을 재귀 호출하여 결과를 A에 저장한다.
- 그 다음에 A를 상,하,좌,우 방향에 대해 가능하면 1번 이동한 뒤, B에 대해 `is_a_winner`를 호출하여 B에 저장한다.
- 이 때 중요한 것은 B가 A인 것 처럼 `aloc`, `bloc` 순서를 바꿔 호출한다.
- `is_a_winner`은 너무 지저분해서 설명을 생략,,,
- A,B 결과에 따라 정답을 리턴

### 🧐 접근에 대한 회고
구현이 매우 까다로워서 놓치는 조건이 많았다.

특히나 이기는 경우는 이동횟수의 최솟값을 구해야 해서 min 메소드를 쓰는데, 그렇지 않은 경우는 max 메소드를 쓰는등 구현 과정에서
논리가 정리되지 않아 큰 혼란이 왔다. 하루종일 고민했는데 해결이 되지 않아서 스스로 구현하는건 포기했고, 내 접근이 맞는지 논리를 확인하고자 구글링을 했다.
## 😎 Solved Code
```python
import copy

def can_win(board, y1, x1, y2, x2):
    # (y1,x1)에 위치한 플레이어가 이길 수 있는지 여부와 최소횟수 계산
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    width = len(board[0])
    height = len(board)
    
    finished = True
    for i in range(4):
        if (0 <= y1 + dy[i] < height) and (0 <= x1 + dx[i] < width): # bound check
            if board[y1+dy[i]][x1+dx[i]]: # 바닥이 있음
                finished = False
    
    if finished:
        return (False, 0) # 이길 수 없고, 현재 위치 기준 0번 이동 가능
    elif x1 == x2 and y1 == y2:
        return (True, 1) # (y1,x1)에서 한 번 이동시 이길 수 있다
    
    minNum, maxNum = 99999, 0
    
    win = False # (y1,x1)에서 이동시 이기는 수가 단 하나라도 존재 하는가?
    for i in range(4):
        newY = y1 + dy[i]
        newX = x1 + dx[i]
        if (0 <= newY < height) and (0 <= newX < width): # bound check
            if board[newY][newX]:
                new_board = copy.deepcopy(board)
                new_board[y1][x1] = 0
                # can_win이 False라면 상대방이 이길 수 없는 것 => 내가 이기는 경우 반드시 존재
                opponent_win, count = can_win(new_board,y2,x2,newY,newX) # (y1,x1)과 (y2,x2) 위치 바꿔서 호출 (A<->B 턴 스위칭)
                if not opponent_win: # 상대가 진다 = 내가 이긴다
                    win = True
                    minNum = min(minNum, count) # 최소의 이동횟수 계산
                else: # 상대가 이긴다 = 내가 진다
                    maxNum = max(maxNum, count) # 최대한 오래 버티기위해 최대 이동횟수 계산
    count = minNum if win else maxNum
    return (win, count+1)
    
def solution(board, aloc, bloc):
    y1,x1 = aloc
    y2,x2 = bloc
    _, answer = can_win(board, y1,x1, y2,x2)
    
    return answer
```

### ❗️ 결과
성공
### 💡 접근
문제의 가장 중요한 조건 중 하나를 다시 보자.
- 이길 수 있는 플레이어는 최대한 빨리 승리하도록 플레이한다.
- 질 수밖에 없는 플레이어는 최대한 오래 버티도록 플레이한다.

그 다음에 다음 상황을 가정해보자.

A가 현재 위치에서 상, 하, 좌, 우로 이동할 수 있고, 이동시 `승패여부`와 `앞으로 몇번만에 이동하여 지거나 이기는지`는 다음과 같다.
- 상 : 패배, 3
- 하 : 패배, 5
- 좌 : 승리, 2
- 우 : 승리, 6

그럼 A는 현재 위치에서 이길 수 있는가? 그렇다. A는 승리할 수 있는 경우의 수 중 `최솟값(좌:2)`+1 = 3번 이동으로 이긴다.
승리가 보장되어있다면 문제 조건대로 `최대한 빨리 승리`해야 하기 때문이다.

그럼 다음 상황도 보자.

A가 현재 위치에서 상,하로 이동할 수 있고, 이동시 `승패여부`와 `앞으로 몇번만에 이동하여 지거나 이기는지`는 다음과 같다.
- 상 : 패배, 5
- 하 : 패배, 8

그럼 A는 현재 위치에서 이길 수 있는가? 이 경우는 아니다. A는 `질수밖에 없는 플레이어`다. 그렇다면 A는 `최댓값(하:8)`+1 = 9번 이동으로 패배한다. 질수밖에 없다면 문제 조건대로 `최대한 오래 버텨`야 하기 때문이다.

이 아이디어를 그대로 재귀함수로 옮기면 된다. 먼저 A에 대해 can_win 함수를 호출하고, 상하좌우에 대해 이동할 수 있으면 can_win을 재귀 호출한다.

이 때 중요한 것은 갱신된 A좌표와, B좌표의 파라미터 위치를 뒤바꿔 호출한다. 그래야만 A와 B의 순서를 번갈아가며 진행할 수 있다.
`can_win`의 base case(종료 조건)는 다음과 같다.
1. 더 이동시 바운더리를 벗어나거나 발판이 없다 -> (False, 0) 리턴
2. 1번은 아니지만 A와 B의 위치가 같다 == 한 번 이동시 발판이 없어져 무조건 이긴다 -> (True, 1) 리턴

리턴 값은 (Bool, Int)형태인데 (승패여부, 횟수)라고 생각하면 된다. 이렇게 Top-Down 형태로 재귀 호출을 하며 Count를 차곡차곡 쌓아나가는 방식이다.

## 🥳 92345 : 사라지는 발판 문제 회고
가장 공들여서 풀어볼려고 하루종일 매달렸지만 실패했던 문제. 재귀함수 구현 문제는 지나고보면 아이디어는 간단한거같은데 구현이 너무 어려운 것 같다. 세상에 이런 문제도 있구나 하고 겸손해지게 되던 문제였다,,,

혼자 힘으로 구현하기 어려워서 구글링 하며 알게된 알고리즘이자 게임 이론이 하나 있다. 바로 MiniMax 알고리즘인데, 이 컨셉이 문제에서 요구하는 상황과 일치한다.

Ref : 

https://going-to-end.tistory.com/entry/Minimax-algorithm-%EB%AF%B8%EB%8B%88%EB%A7%A5%EC%8A%A4-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=jerrypoiu&logNo=221280459884