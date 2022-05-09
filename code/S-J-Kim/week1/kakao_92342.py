import copy

answer = []
max_score = 0
default = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def count_score(arr, info):

    rscore = 0
    ascore = 0

    for i in range(11):
        if arr[i] == info[i] == 0:
            continue

        if arr[i] > info[i]:
            rscore += 10 - i
        else:
            ascore += 10 - i

    return rscore - ascore


def DFS(idx, remains, arr, info):
    global max_score, answer

    if remains == 0:
        tmp_score = count_score(arr, info)

        if max_score <= tmp_score and tmp_score != 0:
            if tmp_score == max_score:
                for j in reversed(range(11)):
                    if answer[j] > arr[j]:
                        break
                    elif answer[j] < arr[j]:
                        answer = copy.deepcopy(arr)
                        break
                    else:
                        continue

            else:
                answer = copy.deepcopy(arr)
            max_score = tmp_score

        return

    if idx == 10:
        arr[idx] = remains
        tmp_score = count_score(arr, info)

        if max_score <= tmp_score and tmp_score != 0:
            if tmp_score == max_score:
                for j in reversed(range(11)):
                    if answer[j] > arr[j]:
                        break
                    elif answer[j] < arr[j]:
                        answer = copy.deepcopy(arr)
                        break
                    else:
                        continue

            else:
                answer = copy.deepcopy(arr)
            max_score = tmp_score

        return

    if info[idx] < remains:
        new_arr = copy.deepcopy(arr)
        new_arr[idx] = info[idx] + 1
        DFS(idx + 1, remains - (info[idx] + 1), new_arr, info)

    DFS(idx + 1, remains, copy.deepcopy(arr), info)


def solution(n, info):
    global default

    for i in range(11):
        DFS(i, n, copy.deepcopy(default), info)

    return answer if not max_score < 1 else [-1]


solution(9, [0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 0])
