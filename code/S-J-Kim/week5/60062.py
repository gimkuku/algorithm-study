from bisect import bisect_right
from itertools import permutations
from copy import deepcopy


def solution(n, weak, dist):
    answer = 987654321
    len_weak = len(weak)

    for point in weak[:]:
        weak.append(point + n)

    for perm in permutations(dist):
        for i in range(len_weak - 1):
            ans = 0
            sliced = deepcopy(weak[i : i + (len_weak)])

            j = 0
            work = 0
            idx = 0

            while ans <= len_weak and j < len(perm):
                work = sliced[idx] + perm[j]
                ans += 1
                idx = bisect_right(sliced, work)

                if idx >= len_weak:
                    break
                j += 1

            if ans <= len_weak and j < len(perm):
                answer = min(answer, ans)

    return answer if answer != 987654321 else -1


solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30])
