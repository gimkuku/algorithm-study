from itertools import combinations
from collections import defaultdict

def solution(info, query):
    result = []
    info_dict = defaultdict(list)
    for i in info:
        i = i.split()
        info_key = i[:-1]
        info_score = int(i[-1])
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_score)
    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split()
        query_score = int(q[-1])
        q = q[:-1]

        for i in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        tmp_q = ''.join(q)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                result.append(len(scores) - start)
        else:
            result.append(0)
    return result
