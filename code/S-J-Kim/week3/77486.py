def solution(enroll, referral, seller, amount):
    answer = {worker: 0 for worker in enroll}
    answer["-"] = 0
    network = {child: parent for (child, parent) in zip(enroll, referral)}

    for (worker, sales) in zip(seller, amount):
        sales *= 100

        answer[worker] += sales

        worker_iter = worker

        while worker_iter != "-" and sales != 0:
            answer[network[worker_iter]] += sales // 10
            answer[worker_iter] -= sales // 10

            worker_iter = network[worker_iter]
            sales //= 10

    del answer["-"]

    return list(answer.values())


solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10],
)
