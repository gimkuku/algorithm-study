def solution(enroll, referral, seller, amount):
    answer = []
    profit_dicts = {}  # 각 인원의 이윤을 저장하는 딕셔너리
    tree_dicts = {}  # child - parent 관계 저장하는 딕셔너리
    for i in range(len(enroll)):
        tree_dicts[enroll[i]] = referral[i]  
        profit_dicts[enroll[i]] = 0  # 이윤 모두 0으로 초기화

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


    for name in enroll :
        answer.append(int(profit_dicts[name]))
    return answer
