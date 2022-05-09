def parse_in_sec(time):

    sec = 0
    hh, mm, ss = time.split(":")
    sec += int(hh) * 60 * 60
    sec += int(mm) * 60
    sec += int(ss)

    return sec


def solution(play_time, adv_time, logs):
    answer = 360001
    ptime_max = -1

    ptime_arr = [0 for _ in range(60 * 60 * 100)]

    ptime_sec = parse_in_sec(play_time)
    atime_sec = parse_in_sec(adv_time)

    for log in logs:
        start, end = log.split("-")
        start = parse_in_sec(start)
        end = parse_in_sec(end)

        ptime_arr[start] += 1
        ptime_arr[end] -= 1

    # ptime_arr[i] = i ~ i+1초간 재생 중인 사람의 수
    for i in range(1, len(ptime_arr)):
        ptime_arr[i] += ptime_arr[i - 1]

    # ptime_arr[i] = 0 ~ i+1초까지의 총 재생 누적시간
    for i in range(1, len(ptime_arr)):
        ptime_arr[i] += ptime_arr[i - 1]

    for i in range(atime_sec - 1, ptime_sec):
        ptime_sum = ptime_arr[i] - ptime_arr[i - atime_sec]

        if ptime_sum > ptime_max:
            ptime_max = ptime_sum
            answer = i - atime_sec

    if answer == 360001:
        answer = 0

    if answer != 0:
        answer += 1

    hh = answer // 3600
    answer -= 3600 * hh
    mm = answer // 60
    answer -= 60 * mm

    answer = f"{hh:02d}:{mm:02d}:{answer:02d}"
    return answer


solution(
    "50:00:00",
    "10:00:00",
    ["00:00:00-38:21:49", "00:00:00-15:36:51", "00:00:00-42:51:45"],
)
