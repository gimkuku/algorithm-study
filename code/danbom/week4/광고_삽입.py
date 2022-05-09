def time_to_sec(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def sec_to_time(sec):
    h = sec // 3600
    h = '0' + str(h) if h < 10 else str(h)
    sec = sec % 3600
    m = sec // 60
    m = '0' + str(m) if m < 10 else str(m)
    sec = sec % 60
    s = '0' + str(sec) if sec < 10 else str(sec)
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)               
    view = [0 for _ in range(play_time + 1)]

    for l in logs:
        start, end = l.split('-')
        start = time_to_sec(start)
        end = time_to_sec(end)
        view[start] += 1
        view[end] -= 1
        
    for i in range(1, len(view)):
        view[i] += view[i - 1]

    for i in range(1, len(view)):
        view[i] += view[i - 1]

    section_view, result = 0, 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if section_view < view[i] - view[i - adv_time]:
                section_view = view[i] - view[i - adv_time]
                result = i - adv_time + 1
        elif section_view < view[i]:
            section_view = view[i]
            result = i - adv_time + 1

    return sec_to_time(result)
