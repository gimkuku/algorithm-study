def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    result = set(report)
    result = list(result)
    
    dict = {}
    for id in id_list:
        dict[id] = []
        
    for i in result:
        show = i.split(" ")
        dict[show[1]] += [show[0]]
        
    for key, value in dict.items():
        if len(value) >= k:
            for person in value:
                answer[id_list.index(person)] += 1
                
    return answer
