def solution(id_list, report, k):
    d = dict()
    for id in id_list:
        d[id] = [0, [], 0]
    
    report = set(report)
    for r in report:
        a, b = r.split(" ")
        d[b][0] += 1
        d[b][1].append(a)
    
    for id in id_list:
        if d[id][0] >= k:
            for i in d[id][1]:
                d[i][2] += 1
                
    answer = []
    for id in id_list:
        answer.append(d[id][2])
    
    return answer