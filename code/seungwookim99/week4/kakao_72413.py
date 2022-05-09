def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)
    distance = [[INF] * (n+1) for _ in range(n+1)] # 비용 INF로 초기화
    
    for i in range(n+1):
        distance[i][i] = 0 # i<->i 비용 0으로 초기화
    
    for i, j, fare in fares: # i<->j 비용이 있으면 해당값으로 갱신
        distance[i][j] = fare
        distance[j][i] = fare
    
    # 플로이드-워셜
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                min_val = min(distance[i][j], distance[i][k] + distance[k][j])
                distance[i][j] = min_val
                distance[j][i] = min_val
    
    answer = INF
    # s->i(합승) + i->a(a 따로) + i->b(b 따로) 최솟값
    for i in range(1,n+1):
        answer = min(distance[s][i] + distance[i][a] + distance[i][b], answer)

    return answer