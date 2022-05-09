from itertools import product
from bisect import bisect_left, bisect_right 

def count_by_range(array, left_value, right_value): 
    right_index = bisect_right(array, right_value) 
    left_index = bisect_left(array, left_value) 
    return right_index - left_index

def get_index(lang, position, career, food):
    return 3*3*3*lang + 3*3*position + 3*career + food

def store_data(lang, position, career, food, score, map_d, info_list):
    for l_, p_, c_, f_ in product([0,1], repeat=4): #(0,0,0,0) ~ (1,1,1,1) 16가지
        l, p, c, f = map_d[lang], map_d[position], map_d[career], map_d[food]
        info_list[get_index(l*l_, p*p_, c*c_, f*f_)].append(int(score))
    return

def solution(info, query):
    answer = []
    info.sort(key=lambda x : int(x.split(" ")[4]))
    map_d = {
        "-": 0,
        "cpp": 1,
        "java": 2,
        "python": 3,
        "backend": 1,
        "frontend": 2,
        "junior": 1,
        "senior": 2,
        "chicken": 1,
        "pizza": 2
    }
    info_list = [[] for _ in range(4*3*3*3)]
    for i in info:
        lang, position, career, food, score = i.split(" ")
        store_data(lang, position, career, food, score, map_d, info_list)
    
    for q in query:
        lang, _, position, _, career, _, food, score = q.split(" ")
        l, p, c, f = map_d[lang], map_d[position], map_d[career], map_d[food]
        idx = get_index(l,p,c,f)
        if not info_list[idx]:
            answer.append(0)
        else:
            count = count_by_range(info_list[idx], int(score), info_list[idx][-1])
            answer.append(count)
    
    return answer