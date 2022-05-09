from collections import defaultdict
from itertools import product
from bisect import bisect_left


def solution(info, query):
    answer = []
    maskarr = list(product([True, False], repeat=4))
    info_dict = defaultdict(list)

    for command in info:
        splited = command.split()
        infomation = splited[:-1]
        for mask in maskarr:
            info_dict[
                "".join(
                    [
                        type_name if mask_bit else "-"
                        for (type_name, mask_bit) in zip(infomation, mask)
                    ]
                )
            ].append(int(splited[-1]))

    for key in info_dict.keys():
        info_dict[key].sort()

    for command in query:
        lang, _, part, __, year, ___, soul, score = command.split()
        key = "".join([lang, part, year, soul])
        ans = bisect_left(info_dict[key], int(score))
        answer.append(len(info_dict[key]) - ans)

    return answer


solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ],
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ],
)
