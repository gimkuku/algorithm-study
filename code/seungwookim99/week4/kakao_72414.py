def hhmmss_to_seconds(hhmmss):
    hh, mm, ss = hhmmss.split(":")
    return int(hh)*3600 + int(mm)*60 + int(ss)

def seconds_to_hhmmss(s):
    hh = str(s//3600)
    mm = str(s%3600//60)
    ss = str(s%3600%60)
    if len(hh) == 1:
        hh = '0' + hh
    if len(mm) == 1:
        mm = '0' + mm
    if len(ss) == 1:
        ss = '0' + ss
    return hh+':'+mm+':'+ss

def get_answer(S, n, l):
    if n == l:
        return 0
    tail_i = 0
    head_i = l-1
    max_count = sum(S[0:l])
    sub_sum = sum(S[0:l])
    start = 0
    while head_i+1 <= n:
        if sub_sum + S[head_i+1] - S[tail_i] > max_count:
            start = tail_i + 1
            max_count = sub_sum + S[head_i+1] - S[tail_i]
        sub_sum += S[head_i+1] - S[tail_i]
        head_i += 1
        tail_i += 1
    return start

def solution(play_time, adv_time, logs):
    answer = ''
    cumulative_sum = [0]*360001
    play_time = hhmmss_to_seconds(play_time)
    adv_time = hhmmss_to_seconds(adv_time)
    
    # 누적합 계산을 위한 시작, 끝 기록
    for log in logs:
        start,end = log.split("-")
        start = hhmmss_to_seconds(start)
        end = hhmmss_to_seconds(end)
        cumulative_sum[start] += 1
        cumulative_sum[end] += -1
    
    # 누적합 계산
    for i in range(1,play_time+1):
        cumulative_sum[i] += cumulative_sum[i-1]
    start_seconds = get_answer(cumulative_sum, play_time, adv_time)
    answer = seconds_to_hhmmss(start_seconds)
    return answer