import copy

sheep_max = -1


def solution(info, edges):
    graph = {i: [] for i in range(len(info))}

    for edge in edges:
        graph[edge[0]].append(edge[1])

    def DFS(node, sheep, wolf, path):
        global sheep_max

        path.remove(node)

        if info[node] == 0:
            sheep += 1

            if sheep > sheep_max:
                sheep_max = sheep

        else:
            wolf += 1

            if wolf >= sheep:
                return

        for child in graph[node]:
            path.append(child)

        for child in path:
            DFS(child, sheep, wolf, copy.deepcopy(path))

    DFS(0, 0, 0, copy.deepcopy([0]))

    return sheep_max


solution(
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]],
)
