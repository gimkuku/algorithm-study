# WIL

# 괄호 변환 (60058)
문제에서 요구하는 것만 잘 구현하면 풀수 있는 문제였습니다.
오랜만에 recursion 파티를 하려니까 잠깐 헷갈렸지만 금방 감 잡았습니다.
늘 recursion break 조건과 예외처리에 촉각을 곤두세워야 할거 같습니다~~

코드에 한줄한줄 주석 달며 과정을 써놨습니당


# 블록 이동하기 (60063)
처음에 생각한대로 풀다보니 이것저것 꼬여서 굉장히 더러운 코드가 되어버렸습니다...! 좌표는 1,1을 0,0으로 가정하여 풀었습니다! new_board 만들기 귀찮..

- 전체적인 방법 : visited를 두개 선언하여 BFS -> 해당 배열은 삼차원으로 선언했습니다.
    - 하나는 로봇이 가로로 있는 경우 visited[0][a][b]
    - 하나는 로봇이 세로로 있는 경우 visited[1][a][b]

## 각 메서드 설명

- check_boundary
    - Return True / False
    - 이동한 위치가 지도 안에 있는지 경계 확인 

- change_rot
    - Return 'h' - 가로 / 'v' - 세로
    - 회전을 하게되면 무조건 방향이 바뀌는데 이 부분을 구현한 메서드

- check_visited
    - Return True / False
    - 이동한 위치가 이전에 방문하지 않았는지 확인
    - 가로(h)이면 visited[0][a][b] 확인 
    - 세로(v)이면 visited[1][a][b] 확인
    - 만약 방문 가능한 곳이면 -> visited True 처리 후 True 반환 (방문처리 통상적인 BFS랑 달리 메서드 안에 넣어서 혼란을 드려 죄송.. bad code..)

- rotation_v(a, b, c, d)
    - 현재 로봇이 세로로 놓여있는 경우 rotation
    - return (회전가능한지(Boolean), 좌표1x, 좌표1y, 좌표2x, 좌표2y)
    1. 회전시 방향이 바뀔 것이기 때문에 change_rot 호출
    2. 해당 메서드는 a,b가 위칸인 경우를 가정하고 만들어졌으므로, a,b가 아래에 있다면 c,d와 swap  --> 이 부분때문에 오래 걸렸습니다.....
    3. 각각의 rotation 실행 
        - rotation 가능하면 (True, 바뀐 좌표) return
        - rotation 불가하면 (False, 원래 좌표) return

- rotation_h(a, b, c, d)
    - 현재 로봇이 가로로 놓여있는 경우 rotation
    - 상위 rotation_v와 로직 동일합니다!!

- bfs
    - 일반적임 BFS!
    - rotation, 상하좌우 움직이기!

결론적으로 굉장히 더러운 코드가 되었습니다. 그래서 일단 타 블로그 보고 좀 정리하고자 합니다!!! 제출 전까지 함 코드 개선이 될지는 모르겠습니다. 개선된 코드는 60063-re.py로 올립니다
(시간이 부족하여 개선된 코드 60063-re는 못올릴거 같네요 ㅠ)



# 가사검색 (60060)
60060.py 와 60060-re.py 두번에 걸쳐서 풀었습니다

처음에는 구한 값들을 dictionary에 메모하여서 똑같은 키워드가 나왔을 때, 다시 계산할 필요 없이 구하는 방식으로 충분히 해결할 수 있다고 생각했습니다. 
    - dic_by_s_word : ?를 제외한 문자가 앞에 있는 경우 memoization
    - dic_by_e_word : ?를 제외한 문자가 뒤에 있는 경우 memoization

1. 어차피 keyword의 문자 길이와 word의 문자 길이가 같아야 성립하는게 1조건이므로, word들을 word 길이 기준으로 분류하여 dictionary에 저장하자 / key (word 길이) : word list
2. queries를 돌면서 각각의 keyword를 검사한다
    * 만약 keyword의 길이와 word의 길이가 같은게 없다면 0을 answer에 저장
    * 만약 keyword가 모두 ? 인 경우, word 길이가 keyword의 길이와 같은 word의 개수를 answer에 저장
3. 물음표가 접두사에 있는 경우와 물음표가 접미사에 있는 경우를 나눔
    * ? 을 제외한 문자를 slice 한다.
    * 각각의 경우의 memo에서 이전 계산 결과 확인 -> 있으면 해당 결과 answer에 저장
    * memo 안되어 있으면 search_start / search_end 수행

- search_start / search_end
    - 키워드 문자열의 개수에 해당하는 word들을 쭉 보면서 (dic_by_len[keyword 개수]) sliced_keyword가 들었는지 탐지


## 문제점

효율성 테스트 케이스 2번에서 시간초과가 발생 ㅠㅠ
search_start 와 search_end 메서드에서 수행하는 과정이 저는 시간 초과라고 추정하는데 맞는지는 잘 모르겠습니다!!

다 맞고 테케 1개만 틀리니까 아주 감질맛나서 어케든 원인을 찾아보려 했으나, 제가 푼 방식에서는 결국 저부분이 걸려서 그냥 갈아엎어야 한다는 결론을 도달했습니다... (혹시 현재 제 코드에서 바꿔서 효율성 테케2를 통과할 방법이 있을 까요..)

결국 블로그들을 뒤져보니 trie? 자료구조로 푸는 방법들이 많더군요
저는 시간이 없어서 현재 제 코드에서 변경을 최소화 할 수 있는 bisect 방법을 택했습니다. 


## 개선 방법

### word들을 오름차순으로 정렬 후 이분 탐색으로 속도 높이기
키워드에서 ? 부분을 a와 z로 변경하여 sort된 배열에 들어갈 위치를 찾아서 사이값들의 개수를 구하는 방식입니다.
* ex) fox??? -> foxaaa / foxzzz 
    * 6자리의 word가 있는 배열 예를 들어 abcefd, cdefsa, foxasb, foxgdx 가 sort된 배열이라고 한다면 bisect_left(배열, 'foxaaa')와 bisect_right(배열, 'foxzzz')를 통해 양쪽 index를 구할 수 있다. 

?가 접미사로 있는 keyword들은 위와 같이 구해주면 되고 ?가 접두사에 있는 keyword들은 거꾸로 문자들을 reverse 하여 구한다. -> 오름차순으로 sort하기 위해서!!!


1. dic_by_len과 dic_by_len_reverse 딕셔너리를 만들어서 word 문자열의 길이에 따른 word 딕셔너리를 끼고 리스트를 만든다. reverse는 문자열을 넣을 때, 뒤집어서 넣는다.
2. dic_by_len과 dic_by_len_reverse를 오름차순으로 sort 한다. 
3. quries를 돌면서 keyword에 대해서 60060.py에서 시도한 검사를 진행한다.
4. search_start / search_end 메소드에서 이분탐색을 하여 개수를 memo하고 return 한다. 


