from collections import deque

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def OOR(newrx, newry, newbx, newby):
    global n, m
    
    if newrx < 0 or newry < 0 or newbx < 0 or newby < 0:
        return True
    if newrx > n-1 or newry > m-1 or newbx > n-1  or newby > m-1 :
        return True
    # print(newrx, newry, n,m)
    return False

def dfs(rx, ry, bx, by, direct, graph,answer):
    global n, m
    rpos = m * rx + ry
    bpos = m * bx + by
    graph = list(graph)
    dx, dy = direct
    newrx, newry, newbx, newby = rx + dx, ry + dy, bx + dx, by + dy
    if graph[rpos] == "#" or OOR(newrx, newry, newbx, newby):
        return -1
        
    flag = -1
    rcnt,bcnt = 0,0
    while True:
        rcnt += 1
        rpos = m * newrx + newry
        if (graph[rpos] == "#") or OOR(newrx, newry, newbx, newby):
            newrx -= dx
            newry -= dy
            break
        if graph[rpos] == "O":
            flag = answer + 1
            break
        newrx += dx
        newry += dy

    graph[m * rx + ry] = '.'
    if flag < 0:
        graph[m * newrx + newry] = "R"
    
    while True:
        bcnt += 1
        bpos = m * newbx + newby
        if (graph[bpos] == "#")or (OOR(newrx, newry, newbx, newby)):
            newbx -= dx
            newby -= dy
            break
        if graph[bpos] == "O":
            return -1
        newbx += dx
        newby += dy

    if flag > 0:
        return flag
    graph[m * bx + by] = '.'
    graph[m * newbx + newby] = 'B'
    
    # 두개가 같은 자리에 있으면 뒤에 있던애 뒤로 빼주기
    if newrx == newbx and newry == newby:
        if rcnt > bcnt:
            newrx -= dx
            newry -= dy
        else:
            newbx -= dx
            newby -= dy

    graph = ''.join(graph)
    return newrx,newry,newbx,newby,graph,answer+1

def solution(_n, _m, graph):
    global n, m
    n = _n
    m = _m
    graph_str = ""
    for i in graph:
        for j in i:
            graph_str += j
    # print(graph_str)
    answer = 0
    rx,ry,bx,by = 0,0,0,0
    for idx,i in enumerate(graph):
        for jdx, j in enumerate(i):
            if j == "R":
                rx = idx
                ry = jdx
            if j == "B":
                bx = idx
                by = jdx

    # R,B 위치 찾기 
    q = deque([(rx,ry,bx,by,dir[0],graph_str,0),(rx,ry,bx,by,dir[1],graph_str,0),(rx,ry,bx,by,dir[2],graph_str,0),(rx,ry,bx,by,dir[3],graph_str,0)])
    visited = []
    while q:
        rx, ry, bx, by, direct, graph, answer = q.popleft()
        visited.append((rx, ry, bx, by, direct, graph))
        a = dfs(rx, ry, bx, by, direct, graph, answer)
        if type(a) == int and a != -1:
            # print(a)
            if a < 11:
                print(a)
                return a
            else:
                print(-1)
                return -1 
        if a != -1:
            # print(a)
            rx, ry, bx, by, graph,answer = a
            for i in range(4):
                if (rx, ry, bx, by, dir[i], graph) not in visited:
                    q.append((rx, ry, bx, by, dir[i], graph, answer))
        if a == -1:
            continue
    print(-1)
    return -1
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

solution(n,m,graph)
