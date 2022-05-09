import math

def time_to_minutes(time):
    h, m = map(int, time.split(':'))
    return h*60 + m

def solution(fees, records):
    answer = []

    dt, df, ut, uf = fees

    dic = dict()

    for r in records:
        time, car, inout = r.split()
        car = int(car)

        if car in dic:
            dic[car].append([time_to_minutes(time), inout])
        else:
            dic[car] = [[time_to_minutes(time), inout]]

    rList = sorted(dic.items())

    for r in rList:
        t = 0

        for rr in r[1]: 
            if rr[1] == "IN": 
                t -= rr[0] 
            else: 
                t += rr[0] 

        if r[1][-1][1] == "IN": 
            t += time_to_minutes('23:59') 

        if t <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((t-dt) / ut) * uf)

    return answer
