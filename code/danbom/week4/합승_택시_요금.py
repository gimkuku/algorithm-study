import sys
import heapq

def solution(n, s, a, b, fares):
    result = sys.maxsize
    graph = [[] for _ in range(n+1)]
    
    for i, j, cost in fares:
        graph[i].append([j, cost])
        graph[j].append([i, cost])
        
    def dijkstra(s, e):
        visit = [sys.maxsize]*(n+1)

        visit[s] = 0

        heap = []
        heapq.heappush(heap, [0, s])

        while heap:
            cost, node = heapq.heappop(heap)

            if cost > visit[node]:
                continue

            for new_node, new_cost in graph[node]:
                new_cost += cost

                if new_cost < visit[new_node]:
                    visit[new_node] = new_cost

                    heapq.heappush(heap, [new_cost, new_node])

        return visit[e]
            
    for i in range(1, n+1):
        result = min(result, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
        
    return result
