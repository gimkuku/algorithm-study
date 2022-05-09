import math

def solution(enroll, referral, seller, amount):
    answer = {name: 0 for name in enroll}
    parent = {'-':'-'}

    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]

    for i in range(len(seller)):
        people = seller[i]
        profit = amount[i]*100
        while people != "-" and profit >= 1:
            answer[people] += math.ceil(profit*0.9)
            profit -= math.ceil(profit*0.9)
            people = parent[people]

    return list(answer.values())
