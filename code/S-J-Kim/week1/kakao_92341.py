from datetime import datetime


def calc_time(start, end):
    start = datetime.strptime(start, "%H:%M")
    end = datetime.strptime(end, "%H:%M")

    return ((end - start).seconds) / 60


def solution(fees, records):
    d_time, d_fee, u_time, u_fee = fees
    answer = []
    parking_log = {}
    parking_dur = {}

    for record in records:
        time, plate, inout = record.split()
        try:
            parking_log[plate].append([time, inout])
        except:
            parking_log[plate] = [[time, inout]]
            parking_dur[plate] = 0

    for log in parking_log:
        if parking_log[log][-1][1] == "IN":
            parking_log[log].append(["23:59", "OUT"])

    for log in parking_log:
        for i in range(0, len(parking_log[log]), 2):
            parking_dur[log] += calc_time(
                parking_log[log][i][0], parking_log[log][i + 1][0]
            )

    parking_dur = sorted(parking_dur.items())

    for (key, val) in parking_dur:
        tmp = d_fee
        val -= d_time

        if val > 0:
            tmp += (val // u_time) * u_fee

            if val % u_time != 0:
                tmp += u_fee

        answer.append(int(tmp))

    return answer
