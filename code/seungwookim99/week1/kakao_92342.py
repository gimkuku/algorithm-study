from itertools import combinations_with_replacement

def get_all_combinations(n):
    comb = []
    for indices in combinations_with_replacement(range(11), n):
        tmp = [0]*11
        for index in indices:
            tmp[index] += 1
        comb.append(tmp)
    return comb

def calc_score_difference(apeach, lion):
    apeach_score, lion_score = 0, 0
    for i in range(11):
        if apeach[i] < lion[i]:
            lion_score += 10-i
        elif apeach[i] == 0 and lion[i] == 0:
            continue
        else:
            apeach_score += 10-i
    return lion_score - apeach_score

def compare_and_get_answer(a,b):
    # 어피치와 같은 점수차를 낼 수 있는 두 list a, b 중
    # 낮은 점수를 더 많이 맞힌 경우를 찾아서 return
    for i in reversed(range(11)):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            return a
        else:
            return b

def solution(n, info):
    answer = []
    max_d_score = -99999 # 점수차 초기화
    for lion_info in get_all_combinations(n):
        d_score = calc_score_difference(info, lion_info)
        if d_score == max_d_score:
            answer = compare_and_get_answer(answer, lion_info)
        elif d_score > max_d_score:
            max_d_score = d_score
            answer = lion_info
        else:
            continue

    if max_d_score <= 0:
        answer = [-1]
    return answer