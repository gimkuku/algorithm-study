<!-- @format -->

# 순위 검색

cpp, java, python 3개를 루트노드로 하는 이진트리 인거같아서 쭉 풀었습니다.

근데 효율성에서 시간초과가 나더라구요..

그 점수를 찾는 과정에서 시간을 줄일 수 있을 것 같아, 이진탐색을 사용하여 해결함 !

직접 구현한 이진탐색은 시간초과 뜨길래, bisect 모듈에 있는걸 사용했따.

## 효율성 해결 방법

find함수 내의 코드

효율성 시간초과 났던 코드

```python
for i, val in enumerate(arr[index]):
    if val >= score:
        return len(arr[index]) - i
```

**효율성 해결 코드**

```python
import bisect as bs

if score == -1:
    return len(arr[index])
return len(arr[index]) - bs.bisect_left(arr[index], score)
```

success!

# 합승 택시 요금

전형적인 플로이드-와샬 문제이다!

bidirectional 하므로 반대로 생각했다

min(A -> S) + min(B -> S) + min(S -> 현재 위치)

```python
for mid in range(1, n+1):
    answer = min(answer, adj[mid][a] + adj[mid][b] + adj[mid][s])
```

success!

# 광고 삽입

누적합 문제!

데이터들을 배열에 잘 넣어주고 누적합을 이용하면 풀 수 있었다.

그러나.. 테스트 케이스 4개정도가 계속 틀림

```python
for log in logs:
    start, end = map(convert_to_int, log.split('-'))
    arr[start] += 1
    if end+1 > play_time:
        continue
    arr[end+1] += (-1) # this

    ... 생략

for i in range(1, play_time+1):
    if adv_time+i > play_time:
        break
    psum[i] = psum[i-1] - arr[i-1] + arr[adv_time+i] # this
```

이 부분이 잘못되었었다. 광고가 끝나는 지점은 포함되면 안되는데, 포함해버린 것이 잘못!!

다음과 같이 고쳐서 맞았다

이런 인덱스가 중요한 문제를 잘 캐치 못하는게 단점인 것 같다.

```python
for log in logs:
    start, end = map(convert_to_int, log.split('-'))
    arr[start] += 1
    if end > play_time:
        continue
    arr[end] += (-1) # this

for i in range(1, play_time+1):
    if adv_time+i > play_time:
        break
    psum[i] = psum[i-1] - arr[i-1] + arr[adv_time+i-1] # this
```
