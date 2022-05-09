def solution(enroll, referral, seller, amount):
    answer = [0] * (len(enroll))
    enroll_dict = {}
    for i in range(len(enroll)):
        enroll_dict[enroll[i]] = i
    for i in range(len(seller)):
        profit = amount[i] * 100
        s = seller[i]
        while s != '-':
            if profit < 10:
                seller_idx = enroll_dict[s]
                answer[seller_idx] += profit
                break
            else:
                commission = int(profit * 0.1)
                profit -= commission
            seller_idx = enroll_dict[s]
            answer[seller_idx] += profit
            profit = commission
            s = referral[seller_idx]
    return answer