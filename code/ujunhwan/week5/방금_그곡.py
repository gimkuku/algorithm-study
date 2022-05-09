def solution(m, musicinfos):
    answer = ''
    
    m = m.replace('A#', 'a')
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    
    def convert_time(str):
        hour, min = map(int, str.split(":"))
        return hour*60+min
        
    def calc_playtime(start, end):
        return abs(convert_time(start)-convert_time(end))
   	
    def sync(time, str):
        str = str.replace("A#", 'a')
        str = str.replace("C#", 'c')
        str = str.replace("D#", 'd')
        str = str.replace("F#", 'f')
        str = str.replace("G#", 'g')
        
        ret = ""
        n = len(str)
        for i in range(time):
            ret += str[i%n]
            
        return ret
    
    t_arr = []
    c_arr = []
    time_arr = []
    
    for musicinfo in musicinfos:
        start, end, title, code = list(musicinfo.split(','))
        time = calc_playtime(start, end)
        code = sync(time, code)
        t_arr.append(title)
        c_arr.append(code)
        time_arr.append(time)
    
    size = len(m)
    c_size = len(c_arr)
    
    # len, index, title
    cand = []
    
    print(f"m : {m}")
    for i in range(c_size):
        code = c_arr[i]
        idx = code.find(m)
        print(idx, code[idx:idx+size])
        if idx != -1 and code[idx:idx+size] == m:
            cand.append([time_arr[i], i, t_arr[i]])
           
    # play time -> first insert
    
    max_time = -1
    for time, idx, title in cand:
        print(time, idx, title)
        if max_time < time:
            max_time = time
            answer = title
    
    if max_time == -1 or answer == '':
        return "(None)"
    return answer