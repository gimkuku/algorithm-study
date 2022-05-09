## 1. 92335 k진수에서 소수 개수 구하기

#### 1) 10진수를 k진수로 바꾸기

```python
    while n:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    
    rev_base = rev_base[::-1]
```

**divmod**(n, k): n을 k로 나눈 몫과 나머지를 제공하는 함수

나머지를 순서대로 저장한 뒤, 순서를 바꾸면 k진수 변환





#### 2) 소수 판별

```python
for j in range(2, int(i**0.5)+1):
            if i%j==0:
                prime = False
                break
```

판별하고자 하는 수의 제곱근에 1을 더한 수로 나누어 떨어지면 합성수, 나누어 떨어지지 않으면 소수

→ 이는 파이썬 **math.sqrt**를 사용해도 좋을 것 같음

 





## 2. 양궁대회

#### 1) 파이썬으로 중복조합 사용

```python
from itertools import combinations_with_replacement

...

def solution(n, info):
	for i in combinations_with_replacement(range(11), n):
        ...
```

**itertools**: 리스트, 튜플, 문자열 등의 요소에서 순열과 조합을 구할 수 있도록 도와주는 라이브러리

**combinations_with_replacement**: 중복조합



+) 

순열: **permutations(iterable,r=None)** #r을 지정하지 않거나 None으로 하면 최대 길이의 순열 리턴,

조합: **combinations(iterable, r)**,

중복순열: **product(*iterables, repeat=1)**)





#### 2) 개수 세기

```python
from collections import Counter

...

 cnt = Counter(i)
        for i in range(11):
            if info[10-i] == 0 and cnt[i] == 0:
                continue
            if info[10-i] >= cnt[i]:
                a_score += i
            else:
                l_score += i
```

**Counter**: 항목의 개수를 셀 때 사용하는 클래스

ex) Counter('abbcccdddd')

Counter({'d': 4, 'c': 3, 'b': 2, 'a': 1})



+) Counter 클래스의 메소드

1. **most_common()**

 - () 안의 인자만큼 상위 요소를 출력
 - 인자가 없는 경우, 전체 요소가 출력

```python
Counter('abbcccdddd').most_common(1)

[('d', 4)]
```



2. **카운터끼리의 덧셈, 뺄셈**(+, -)

 - 덧셈: 같은 key값을 가진 카운터 값끼리는 더하고 한 카운터에만 있는 key에 대한 값은 그대로 포함
 - 뺄셈: - 기호 앞 카운터를 기준으로, 같은 key값을 가진 카운터 값끼리는 빼고 앞 카운터에만 있는 key값에 대해서는 그대로, 뒤 카운터에만 있는 key값에 대해서는 쓰지 않음

```python
acounter = Counter(['a', 'b', 'a', 'a'])
bcounter = Counter(['c', 'a', 'a'])

acounter + bcounter
Counter({'a': 5, 'b': 1, 'c': 1})

acounter - bcounter    # acounter가 기준 ('c'는 고려할 필요가 없음)
Counter({'a': 1, 'b': 1})
```



3. **subtract()**

 - 2의 뺄셈과는 다르게 각 요소의 값을 뺌
 - 각 요소의 값이 마이너스가 될 수 있음

```python
acounter = Counter(['a', 'b', 'a', 'a'])
bcounter = Counter(['c', 'a', 'a'])

acounter.subtract(bcounter)
Counter({'a': 1, 'b': 1 ,'c': -1})
```



4. **&(교집합), |(합집합)**

```python
acounter = Counter(['a', 'b', 'a', 'a']
bcounter = Counter(['c', 'a', 'a'])

acounter & bcounter
Counter({'a': 2})
       
acounter | bcounter
Counter({'a': 3, 'b': 1, 'c': 1})
```



5. **elements()**

 - 카운터된 숫자만큼 요소 반환

```python
cnt = Counter(a=5, b=3)

list(cnt.elements())
['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b']

list(cnt)
['a', 'b']
```





## 3. 주차 요금 계산

#### 1) 반올림

```python
import math

math.ceil((t-dt) / ut)
```

**ceil**: 반올림하여 정수 반환



+) **floor**: 반내림하여 정수 반환







### 회고

1. 알고리즘 스터디나 코딩테스트 준비 자체를 처음 해보면서 가장 크게 느낀 점은 문법부터 다시 .. 공부해야 겠다는 것이다.
2. 자료구조 공부도 다시......... 해야 겠다.
3. 한 함수에 모든 코드를 작성하는 것보다 여러 함수로 쪼개서 작성하는 것이 메인 함수에서의 가독성에 더 좋은 것 같다.
