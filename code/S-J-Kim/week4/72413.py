def solution(n, s, a, b, fares):
    answer = 99999999
    INF = 9999999
    adjarr = [[0 if i == j else INF for i in range(n)] for j in range(n)]

    for v1, v2, fare in fares:
        adjarr[v1 - 1][v2 - 1] = adjarr[v2 - 1][v1 - 1] = fare

    for i in range(n):
        for j in range(n):
            for k in range(n):
                adjarr[k][j] = min(adjarr[k][j], adjarr[k][i] + adjarr[i][j])

    for i in range(n):
        answer = min(answer, adjarr[s - 1][i] + adjarr[i][a - 1] + adjarr[i][b - 1])

    return answer


solution(
    6,
    4,
    6,
    2,
    [
        [4, 1, 10],
        [3, 5, 24],
        [5, 6, 2],
        [3, 1, 41],
        [5, 1, 24],
        [4, 6, 50],
        [2, 4, 66],
        [2, 3, 22],
        [1, 6, 25],
    ],
)
