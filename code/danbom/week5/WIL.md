이번 주는 리드미 작성 시간이 부족한 관계로 알고리즘 스터디를 하며 이번 문제에 도움이 된 부분만 우선 적어올리도록 하겠습니다..!
1. 카드 짝 맞추기
```python
from collections import defaultdict, deque # week4 순위검색 문제를 풀면서 새롭게 알게된 defaultdict 사용
from itertools import permutations

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
_min = float('inf') # week4 합승 택시 요금 문제 코드 리뷰를 하며 배운 가장 큰 값 지정법 사용 
# https://github.com/gimkuku/algorithm-study/pull/25#discussion_r840621539

def solution(board, r, c):
    global _min # 코드 리뷰 하며 알게된 global 
```
<br />

3. 방금그곡
```python
    for info in musicinfos:
        start, end, title, code = info.split(",")
        
        hh, mm = map(int, start.split(":")) # week4 광고 삽입 코드 리뷰하며 배운 방법 활용
        # https://github.com/gimkuku/algorithm-study/pull/25#discussion_r840551746
        start = hh * 60 + mm
        
        hh, mm = map(int, end.split(":"))
        end = hh * 60 + mm
        duration = end - start
        
        code = change(code)
        code *= int(duration / len(code)) + 1 if not ( duration % len(code) == 0 ) else int(duration / len(code)) 
        # week3 다단계 칫솔 판매 문제 피드백으로 알게된 math 라이브러리 사용하지 않고 올림하는 방법 사용 
        # https://github.com/gimkuku/algorithm-study/pull/22#discussion_r834147609
```
<br />
