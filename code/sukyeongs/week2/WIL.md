## 1. 양과 늑대

#### 1) DFS(깊이 우선 탐색)

```python
def dfs(sheep, wolf, current, path): 
        
        if info[current]:
            wolf += 1
        else:
            sheep += 1 
        
	# 늑대가 다 잡을 경우 0    
        if sheep <= wolf:
            return 0 
        
        maxSheep = sheep 
        
	# 백트래킹 적용
        for p in path: 
            for n in nextNodes(p): 
                if n not in path: 
                    path.append(n) 
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n, path))
                    path.pop() 
                    
        return maxSheep
```

양의 수와 늑대 수를 매번 비교하다가 같아질 때 return 하도록 구현했음.

(사실 이게 괜찮은 방법인지는 모르겠음 ㅠㅠ)

#### 2) 함수 안에 함수 선언

```python
def solution(info, edges):
    
    def nextNodes(v):
        temp = list()
        for e in edges:
            i, j = e 
            if v == i:
                temp.append(j)
        return temp

		def dfs(sheep, wolf, current, path): 
         if info[current]:
            wolf += 1
		...
```

nextNodes 함수에서 edges 매개변수를, dfs 함수에서 info 매개변수를 쓰고 싶은데 여러번 선언하기 귀찮아서 함수 안에 함수가 들어가게끔 했더니 돌아가서 신기했음! 앞으로 자주 사용할 것 같음.

## 2. 파괴되지 않은 건물

효율성 테스트에서 통과를 못해서... 대체 왜 그럴까 하고 찾아보니 “누적합”을 사용해서 풀어야 한다고 함....!!

#### 1) lambda

```python
for row in board:
        answer += len(list(filter(lambda x: x > 0, row)))
```

코딩 테스트가 처음이라 설레는 마음으로 파이썬 문법 공부를 하다가 발견한 함수😊

**lambda 매개변수 : 표현식**

ex) 두 수를 더하는 함수

```python
def hap(x, y):
	return x+y

>>> hap(10,20)
30
```

이 함수를 lambda로 표현하면

```python
>>> (lambda x,y: x+y)(10,20)
30
```

함수 선언 없이 코드를 간결하게 쓸 수 있음!

한번만 사용하는 것이라면 람다 함수를 사용하고,

여러번 호출하는 코드는 함수를 따로 만드는 것이 좋을 것 같음!

그치만.. 일단 효율성 테스트 통과 먼저 좀 ㅋㅋ.....

## 3. 신고 결과 받기

#### 1) 중복 제거 **set()**

```python
result = set(report)
```

#### 2) 신고된 사람 Dictionary에 저장

```python
for i in result:
        show = i.split(" ")
        dict[show[1]] += [show[0]]
```

**split():** ()안의 요소를 기준으로 분할하는 함수
