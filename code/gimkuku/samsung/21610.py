from collections import deque
def solution(n,m,board,cloud_dir):
    dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    # 비 바라기
    cloud = deque([[n-1,0],[n-1,1],[n-2,0],[n-2,1]])
    visited = [[0 for i in range(n)]for j in range(n)]

    # 구름 이동
    for _m in range(m):
        d,s = cloud_dir[_m]
        dx, dy = dirs[d-1]
        _cloud = len(cloud)
        for idx in range(0, _cloud):
            cloud[idx][0] = (cloud[idx][0] + (dx*s)) % n
            cloud[idx][1] = (cloud[idx][1] + (dy*s)) % n

        # 비 내림
        for idx in range(0, _cloud):
            x, y = cloud[idx]
            board[x][y] += 1
            visited[x][y] =1

        # 구름 사라짐
        prev_cloud = _cloud

        water_d = [(1,1),(1,-1),(-1,1),(-1,-1)]
        # 물 복사
        for idx in range(0,prev_cloud):
            x, y = cloud[idx]
            w = 0
            for dx, dy in water_d:
                if x+dx < 0 or x+dx > n-1 or y+dy <0 or y+dy > n-1 : continue
                else:
                    if board[x+dx][y+dy]: w += 1
            board[x][y] += w

        # 새 구름 탄생
        for i in range(n):
            for j in range(n):
                flag = True
                if visited[i][j] :
                    visited[i][j] = 0
                    continue
                if board[i][j] >= 2 and flag:
                    cloud.append([i,j])
                    board[i][j] -= 2

        for i in range(prev_cloud):
            cloud.popleft()

    answer = 0
    for i in range(n):
        for j in range(n):
            answer += board[i][j]
    print(answer)

n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
cloud_dir = []
for i in range(m):
    cloud_dir.append(list(map(int,input().split())))
solution(n,m,board,cloud_dir)