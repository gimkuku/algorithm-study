from collections import deque

def solution(n, day):
    q = deque([])
    answer = 0
    for i in range(1,n+1):
        q.append((i, day[i][0], day[i][1]))
    # print(q)
    while q:
        i, time, value = q.popleft()
        # print(i, time, value)
        if i + time <= n + 1:
            if answer < value:
                answer = value
            for j in range(i+time,n+1):
                if (j, day[j][0], value + day[j][1]) not in q:
                    q.append((j, day[j][0], value + day[j][1]))
        else:
            continue
    print(answer)
n = int(input())
day = [[0,0]]
for i in range(n):
    day.append(list(map(int, input().split())))
solution(n,day)