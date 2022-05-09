from itertools import permutations

def count_friend(dist, weak, n):
    global MIN_NUM
    for i in range(len(weak)):
        new_weak = weak[i:]
        tmp = []
        for j in weak[:i]:
            tmp.append(j+n)
        new_weak += tmp
        count = 1
        cover_range = new_weak[0] + dist[0]
        for w in new_weak[1:]:
            if w <= cover_range:
                continue
            else:
                if count == len(dist):
                    count = int(1e9)
                    break
                cover_range = w + dist[count]
                count += 1
        MIN_NUM = min(MIN_NUM, count)

def solution(n, weak, dist):
    global MIN_NUM
    MIN_NUM = int(1e9)
    for i in range(1,len(dist)+1):
        for d in permutations(dist, i):
            count_friend(d, weak, n)
    return MIN_NUM if MIN_NUM != int(1e9) else -1