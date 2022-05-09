from collections import deque
from copy import deepcopy
answer = 0
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(graphlist, direct):
    graph = deepcopy(graphlist)
    global n
    _max = 0
    dx, dy = direct
    if dx == -1:
        for i in range(n):
            for status in range(1,n):
                # print(i,status)
                if status+dx < 0:
                    continue
                temp = status
                before = graph[n*i + temp]
                if graph[n * i + (temp + dx)] == before:
                    graph[n * i + temp] = 0
                    graph[n * i + (temp + dx)] = before * 2
                    temp += dx
                while True:
                    before = graph[n* temp + i]
                    if temp == -1 or temp == n: break
                    if graph[n * i + (temp + dx)] == 0:
                        graph[n * i + temp] = 0
                        graph[n * i + (temp + dx)] = before
                        temp += dx
                    elif graph[n * i + (temp + dx)] == before:
                        graph[n * i + temp] = 0
                        graph[n * i + (temp + dx)] = before * 2
                        break
                    else: break

    if dy == -1:
        for i in range(n):
            for status in range(1,n):
                if status+dy < 0:
                    continue
                temp = status
                before = graph[n* temp + i]
                
                if graph[n *(temp + dy) + i] == before:
                    graph[n *temp + i] = 0
                    graph[n * (temp + dy) + i] = before * 2
                    temp += dy
                while True:
                    before = graph[n* temp + i]
                    if temp == -1 or temp == n: break
                    # print(temp)
                    if graph[n *(temp + dy) + i] == 0:
                        graph[n *temp + i] = 0
                        graph[n * (temp + dy) + i] = before
                        temp += dy
                    elif graph[n *(temp + dy) + i] == before:
                        graph[n *temp + i] = 0
                        graph[n * (temp + dy) + i] = before * 2
                        break
                    else:
                        break
    if dx == 1:
        for i in range(n):
            for status in range(n-1,-1,-1):
                if status+dx > n-1:
                    continue
                temp = status
                before = graph[n*i + temp]
                
                if graph[n * i + (temp + dx)] == before:
                    graph[n * i + temp] = 0
                    graph[n * i + (temp + dx)] = before * 2
                    temp += dx
                while True:
                    before = graph[n* temp + i]
                    if temp == -1 or temp == n-1: break
                    # print(temp)
                    elif graph[n * i + (temp + dx)] == 0:
                        graph[n * i + temp] = 0
                        graph[n * i + (temp + dx)] = before
                        temp += dx
                    elif graph[n * i + (temp + dx)] == before:
                        graph[n * i + temp] = 0
                        graph[n * i + (temp + dx)] = before * 2
                        break
                    else:
                        break
    if dy == 1:
         for i in range(n):
            for status in range(n-1,-1,-1):
                if status+dy > n-1:
                    continue
                temp = status
                before = graph[n* temp + i]
                if graph[n *(temp + dy) + i] == before:
                    graph[n *temp + i] = 0
                    graph[n * (temp + dy) + i] = before * 2
                    temp += dy
                while True:
                    before = graph[n* temp + i]
                    if temp == -1 or temp == n-1: break
                    elif graph[n *(temp + dy) + i] == 0:
                        graph[n *temp + i] = 0
                        graph[n * (temp + dy) + i] = before
                        temp += dy
                    elif graph[n *(temp + dy) + i] == before:
                        graph[n *temp + i] = 0
                        graph[n * (temp + dy) + i] = before * 2
                        break
                    else:
                        break
    _max = 0
    
    for i in graph:
        if _max < i:
            _max = i
    return _max, graph

def solution(_n, graph):
    global n
    answer = 0
    # graph string으로 만들기
    # print(graph)
    

    q = deque([(graph, dir[0], 0), (graph, dir[1],0), (graph, dir[2],0), (graph, dir[3],0)])
    visited = []

    while q:
        
        a_graph, direct,cnt = q.popleft()
        visited.append((a_graph,direct))
        _max, graph = move(a_graph, direct)
        # if _max > answer:
        #     print(graph,direct, cnt)
        answer = max(answer, _max)
        if cnt < 5:
            cnt += 1
            for i in range(4):
                if (graph, dir[i]) not in visited:
                    # print(graph,dir[i],cnt)
                    q.append((graph,dir[i],cnt))

    print(answer)
    return answer



n = int(input())
graph = []
for i in range(n):
    a = input().split()
    for j in a:
        graph.append(int(j))
solution(n, graph)
