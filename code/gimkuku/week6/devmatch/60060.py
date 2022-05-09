def solution(words, queries):
    answer = []
    for q in queries:
        cnt = 0
        total_len = len(q)
        k = q.replace("?","")
        k_idx = q.find(k)
        for word in words:
            if len(word) != total_len:
                continue
            if k == "":
                cnt+=1
                continue
            idx = word.find(k, k_idx)
            if idx == k_idx:
                cnt+=1
        answer.append(cnt)
                
    return answer