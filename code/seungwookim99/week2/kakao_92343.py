def update_candidates(candidates, graph, visited):
    # 현재 인접한 노드 (candidates)에 대해 방문한 노드(visited)를 고려해 새로운 인접 노드 리스트 계산
    # ex. 예시 1 경우에서 candidates : {1,8}, visited: {0,1} -> return {2,4,8}
    candidates_set = set(candidates)
    for i in visited:
        candidate_set = set(graph[i])
        candidates_set |= candidate_set
    candidates_set -= set(visited)
    return list(candidates_set)

def dfs(candidates, graph, sheep, wolves, info, visited):
    '''
    candidates : 인접 노드 리스트
    graph : 그래프 정보
    sheep : 현재까지 모은 양의 수
    wolves : 현재까지 따라온 늑대 수
    visited : 현재까지 방문한 노드
    '''
    global MAX_NUM
    
    # 방문한 적 없는 인접 노드에 양이 존재하지 않을 때까지 노드 방문 후 인접 노드 리스트 갱신
    new_sheep_num = 0
    while True:
        flag = True
        for i in candidates:
            if info[i] == 0: # 양이 있다면
                new_sheep_num += 1 # 모을 수 있는 양 1마리 추가
                visited.append(i) # 해당 노드는 방문처리
        candidates = update_candidates(candidates, graph, visited) # 새로운 인접 노드 리스트 갱신
        for i in candidates:
            if info[i] == 0: # 만약 갱신된 인접 노드에 양이 존재한다면
                flag = False # while문 다시 수행
        if flag :
            break # 더이상 인접 노드에 양이 없다면 반복문 탈출
    
    # 더 이상 이동할 노드가 없거나 or 이동시 늑대에게 모두 잡아먹힌다면 return
    if not candidates or sheep + new_sheep_num - wolves == 1:
        if  MAX_NUM < sheep + new_sheep_num: # MAX_NUM 과 비교 후 갱신
            MAX_NUM = sheep + new_sheep_num
        return
    
    # 인접한 노드에 늑대밖에 없는 상황. 탐색할 후보 노드(candidates) 업데이트 후 탐색
    for i in candidates:
        new_candidates = update_candidates(candidates, graph, visited + [i]) # i 노드를 방문했다 가정하고 인접노드 갱신
        dfs(new_candidates, graph, sheep + new_sheep_num, wolves + 1, info, visited + [i])
    
    return

def solution(info, edges):
    global MAX_NUM
    graph = [[] for _ in range(18)]
    
    # 그래프 정보 저장
    for from_node, to_node in edges:
        graph[from_node].append(to_node)
        graph[to_node].append(from_node)
    
    # 최대 양 개수 초기화 (시작시 1마리)
    MAX_NUM = 1
    dfs(graph[0],graph,1,0,info,[0])
    return MAX_NUM