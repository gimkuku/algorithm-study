from itertools import permutations


def solution(n, weak, dist):

    weak_size = len(weak)
    # 한 방향으로 만들어주기 위한 배열 키우기
    for i in range(weak_size):
        weak.append(n+weak[i])
    
    answer = len(dist) + 1
    
    friends_order = list(permutations(dist, len(dist)))
    
    for i in range(0, weak_size):
        
        # 점검 리스트 만들기
        check_list = [weak[j] for j in range(i, i+weak_size)]
        
        for order in friends_order:
            # 친구 순열 돌면서 확인
            fidx, cnt = 0, 1
            
            # 순열의 첫 친구가 갈 수 있는 거리
            friend_go = check_list[0] + order[fidx]
            
            for j in range(weak_size):
                
                # 못 다다른 경우
                if check_list[j] > friend_go:
                    # 다음 친구 불러오기
                    fidx += 1
                    cnt += 1
                    if fidx > len(order)-1:
                        break
                    friend_go = check_list[j] + order[fidx]
                    
                    
            answer = min(answer, cnt)
            
            
    
    if answer > len(dist):
        return -1
    else:
        return answer