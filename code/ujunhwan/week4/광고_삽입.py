def solution(play_time, adv_time, logs):
    def convert_to_str(integer):
        h, mod = divmod(integer, 3600)
        m, s = divmod(mod, 60)
        
        hs, ms, ss = str(h), str(m), str(s)
        
        if h < 10:
            hs = "0" + hs
        
        if m < 10:
            ms = "0" + ms
        
        if s < 10:
            ss = "0" + ss
            
        return f"{hs}:{ms}:{ss}"
   	
    def convert_to_int(str):
        h, m, s = map(int, str.split(':'))
        return h*3600+m*60+s
    
    play_time = convert_to_int(play_time)
    adv_time = convert_to_int(adv_time)
    
    arr = [0] * (play_time+1)
    psum = [0] * (play_time+1)
    
    for log in logs:
        start, end = map(convert_to_int, log.split('-'))
        arr[start] += 1
        if end > play_time:
            continue
        arr[end] += (-1)
    
    for i in range(1, play_time+1):
        arr[i] += arr[i-1]
        
    for i in range(0, adv_time+1):
        psum[0] += arr[i]
    
    for i in range(1, play_time+1):
        if adv_time+i > play_time:
            break
        psum[i] = psum[i-1] - arr[i-1] + arr[adv_time+i-1]
    
    answer = 0
    max_value = -1
    for i in range(0, play_time-adv_time+1):
        if max_value < psum[i]:
            max_value = psum[i]
            answer = i
    
    return convert_to_str(answer)