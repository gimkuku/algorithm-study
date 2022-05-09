import bisect as bs

def solution(info, query):
    answer = []
    
    dic = {'-' : -1, 'cpp': 0, 'java': 1, 'python': 2, 'backend': 0, 'frontend': 1, 'junior': 0, 'senior': 1, 'chicken': 0, 'pizza': 1}
    
    size = len(info)
    
    cpp = [[] for col in range(8)]
    java = [[] for col in range(8)]
    py = [[] for col in range(8)]
    
    def save(arr, level, index, data):
        if level == 3:
            arr[index].append(data[level])
            return
        save(arr, level+1, index*2+data[level], data)
        
    def find(arr, level, index, data):
        if level == 3:
            score = data[level]
            if score == -1:
                return len(arr[index])
            return len(arr[index]) - bs.bisect_left(arr[index], score)
        if data[level] == -1:
            return find(arr, level+1, index*2, data) + find(arr, level+1, index*2+1, data)
        return find(arr, level+1, index*2+data[level], data)
    
    for comp in info:
        c = comp.split()
        lang, field, career, food, score = comp.split()
        
        lang = dic[lang]
        field = dic[field]
        career = dic[career]
        food = dic[food]
        score = int(score)
        
        data = [field, career, food, score]
        
        if lang == 0:
            save(cpp, 0, 0, data)
        elif lang == 1:
            save(java, 0, 0, data)
        elif lang == 2:
            save(py, 0, 0, data)
    
    for a in cpp:
        a.sort()
    for a in java:
        a.sort()
    for a in py:
        a.sort()
    
    for q in query:
        q = q.replace('and', ' ')
        q = q.split()
        lang = dic[q.pop(0)]
        data = [dic[q[0]], dic[q[1]], dic[q[2]], int(q[3])]
        if lang == -1:
            answer.append(find(cpp, 0, 0, data)+find(java, 0, 0, data)+find(py, 0, 0, data))
        elif lang == 0:
            answer.append(find(cpp, 0, 0, data))
        elif lang == 1:
            answer.append(find(java, 0, 0, data))
        elif lang == 2:
            answer.append(find(py, 0, 0, data))
    return answer