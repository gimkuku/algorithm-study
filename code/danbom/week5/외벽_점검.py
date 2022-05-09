from itertools import permutations

def check(weak, dist):
    i = 0
    for d in dist:
        bound = weak[i]+d
        while bound >= weak[i]:
            i += 1
            if i == len(weak):
                return True
    return False

def solution(n, weak, dist):
    if not weak:
        return 0

    for m in range(1, len(dist)+1):
        for p in permutations(dist, m):
            new_weak = weak[:]
            for _ in range(len(weak)):
                if check(new_weak, p):
                    return m
                new_weak = new_weak[1:] + [n + new_weak[0]]
    return -1
