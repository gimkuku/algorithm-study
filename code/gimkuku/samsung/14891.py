from collections import deque
def checkrotate(i,d,possible,_visit):
    possible.append([i,d])
    visit = _visit[:]
    visit.append(i)
    if i == 0:
        if c[i][2] != c[i+1][6] and (i+1 not in visit):
            checkrotate(i+1,-d,possible,visit)
    elif i == 3:
        if c[i][6] != c[i-1][2] and (i-1 not in visit):
            checkrotate(i-1,-d,possible,visit)
    else:
        if c[i][2] != c[i + 1][6] and (i + 1 not in visit):
            checkrotate(i+1,-d,possible,visit)
        if c[i][6] != c[i-1][2] and (i - 1 not in visit):
            checkrotate(i-1,-d,possible,visit)
    return 

def rotate(pos):
    for possible in pos:
        i,d = possible
        if d == -1:
            element = c[i].popleft()
            c[i].append(element)
            # print(i+1,"번 반시계방향 회전", c)
        else:
            element = c[i].pop()
            c[i].appendleft(element)
            # print(i+1,"번 시계방향 회전",c)
    return 
            


def solution(_c, order):
    global c,pos
    c = _c
    answer = 0
    for i in order:
        pos = []
        checkrotate(i[0] - 1, i[1], pos, [])
        rotate(pos)

    for i in range(4):
        if c[i][0] == '1':
            answer += 2 ** i
            
    print(answer)
    return answer





c = []
for i in range(4):
    element = deque()
    temp = input()
    for j in range(8):
        element.append(temp[j])
    c.append(element)

n = int(input())
order = []
for i in range(n):
    order.append(list(map(int, input().split())))
    
solution(c,order)