## 행렬 테두리 회전
- 쉬워보여서 도전했는데 생각보다 귀찮은 문제였음..
- 어디서 어디로 대입을 해야하는지를 꼼꼼하게 체크하자
- 가로 세로 헷갈리지 않도록 명확한 기준을 잡는 것이 중요


## 사라지는 발판
- ㅎㅎ 진짜 어려웡..
- MinMax Algorithm 사용 
>  MinMax Algorithm 
>
> 두명이 돌아가면서 작업을 하는 과정에서, 각자 자신이 이길 수 있는 최선의 선택을 할 때 필요한 알고리즘


**내가 푼 방법**
```
*단어 정리*
state : 현재 상태
now_player : 현재 움직이는 사람
step : 몇 스텝만에 이겼는지 
```

1. 현재 플레이어를 상하좌우로 움직인 뒤, 현재 플레이어와 상대 플레이어의 `parameter의 순서를 바꿔서` play함수를  부름 
```
다음 턴에서는 상대방 플레이어가 주 플레이어가 됨
play(주플레이어x, 주플레이어y, 상대플레이어x, 상대플레이어y ) 

<- 이런식으로 부르는데 주 플레이어와 상대 플레이어가 회차별로 바뀌므로 parameter 순서를 바꿔주어야 함! 
```

2. 만약 더이상 갈 곳이 없다면 
= 상하좌우로 for문을 돌렸는데 play함수를 부르지 못했다면 or 내가 있던 자리가 사라졌다면

```
내가 진 상태로 return
```

3. 리턴 될 때, 이긴 사람이 누구인지를 함께 리턴함
``` 
A가 이긴 사람이면 : True
B가 이긴 사람이면 : False
```

4. for문안에서 play 함수가 불렸고, play함수에서 리턴된 값이 돌아왔다면? 
```
1) 현재 내가 지고 있는데, 리턴된 값은 내가 이기는 방법이면
- 현재 내가 이기는 방법으로 update

2) 현재 내가 지고 있는데, 리턴된 값도 내가 지는 방법이면
- 더 오래 버티는 방법 : Max 값으로 update

3) 현재 내가 이기고 있는데, 리턴된 값도 내가 이기는 방법이면
- 더 빨리 이기는 방법 : Min 값으로 update

4) 현재 내가 이기고 있는데, 리턴된 값은 내가 지는 방법이라면
- 무시
```


**회고**
- Minmax Algorithm이라는 이름이 있기는 하지만, 결국은 완전 탐색을 베이스로 한 알고리즘 이기 때문에, 굳이 저 용어를 모르더라도 충분히 풀 수 있었던 문제였던 것 같다.
- 쫄지말고 천천히 다 탐색하는 게 중요했었는듯! 


## 다단계 칫솔 판매
- 3단계 치고는 쉽지 않았나..
- 계속 시간 초과가 나서 찾아보니 share가 0이 되면 멈추라고 하던데.. 나는 멈추는데도 계속 시간초과가 났다. 
- 그래서, list.index(name)함수로 인덱스 번호 찾던걸, dictionary로 변경하니 시간 초과가 안걸렸다. 
- dictionary가 확실히 빠르고 효율성이 좋은 듯.. 애용하자 ..ㅎㅋ


**내가 푼 방법**
1. seller 를 for문을 돌려서 하나씩 answer에 이익을 더해준다. 
2. 이때 seller의 referral이 존재하면 while문으로 계속 referral을 검색해서 계속 추천인들의 이익을 더해준다. 
3. referral이 - 이거나 share가 0이 되면 중지!

