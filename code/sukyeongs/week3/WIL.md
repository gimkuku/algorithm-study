## 1. 사라지는 발판

```python
n,m = 0,0
move = [(0,1),(0,-1),(1,0),(-1,0)]
visit = [[0]*5 for _ in range(5)]

def outOfRange(x,y):
    return x < 0 or x >= n or y < 0 or y >= m

def play(board,curx,cury,opx,opy):
    global visit
    canWin = 0
    
    if visit[curx][cury]: 
        return 0

    for m in move:
        dx, dy = m
        nx, ny = curx + dx, cury + dy
        
        if outOfRange(nx,ny) or visit[nx][ny] or board[nx][ny] == 0 : continue
        
        # 방문
        visit[curx][cury] = 1
        opResult = play(board,opx,opy,nx,ny)+1
        
        # 방문처리 끝
        visit[curx][cury] = 0

        # 현재 저장된 값 패배, 상대가 졌다고 하면 이기는 경우로 저장
        if canWin % 2 == 0 and opResult % 2 == 1 : 
            canWin = opResult
            
        # 현재 저장된 값 패배, 상대가 이겼다고 하면 최대한 늦게 지는 횟수 선택
        elif canWin % 2 == 0 and opResult % 2 == 0 : 
            canWin = max(canWin,opResult)
            
        # 현재 저장된 값 승리, 상대가 졌다고 하면 최대한 빨리 이기는 횟수 선택
        elif canWin % 2 == 1 and opResult % 2 == 1 : 
            canWin = min(canWin,opResult)
            
    return canWin

def solution(board, aloc, bloc):
    global n,m
    n, m = len(board), len(board[0])
    return play(board,aloc[0],aloc[1],bloc[0],bloc[1])
```

## 2. 행렬 테두리 회전하기

#### 1) 회전하는 틀의 모서리 값 temp에 저장

temp1, 2, 3을 임시로 저장하고, 회전하면서 가장 작은 값 도출

```python
for query in queries:
        x1, y1, x2, y2 = query
        temp1 = graph[x1 - 1][y2 - 1]
        temp2 = graph[x2 - 1][y2 - 1]
        temp3 = graph[x2 - 1][y1 - 1]
```

## 3. 다단계 칫솔 판매

 #### 1) dictionary 사용

```python
profit_dicts = {}  # 각 인원의 이윤을 저장하는 딕셔너리
tree_dicts = {}  # child - parent 관계 저장하는 딕셔너리
```

지난 주와 비슷하게 딕셔너리 형태를 사용했음. 각 인원의 이윤과 “Mary”: “-”처럼 enroll과 referral 관계를 딕셔너리로 정의했음.

#### 2) seller 배열을 순회하며 cost 업데이트

```python
for i in range(len(seller)) :
        cost = amount[i]*100
        node = seller[i]
        while node != '-':  # root 노드가 아닌 경우 실행
            parent = tree_dicts[node]
            if cost*0.1 < 1:  # 1원보다 작은 경우 부모에게 이윤 가지 않음
                profit_dicts[node] += cost
                break
            profit_dicts[node] += (cost-(cost//10))
            cost //= 10
            node = parent
```

child에서 parent까지 cost 업데이트
