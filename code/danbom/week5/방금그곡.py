def change(s):
    return s.replace("C#", "H").replace("D#", "I").replace("F#", "J").replace("G#", "K").replace("A#", "L")

def solution(m, musicinfos):
    answer = ""
    m = change(m)
    
    for info in musicinfos:
        start, end, title, code = info.split(",")
        
        hh, mm = map(int, start.split(":"))
        start = hh * 60 + mm
        
        hh, mm = map(int, end.split(":"))
        end = hh * 60 + mm
        duration = end - start
        
        code = change(code)
        code *= int(duration / len(code)) + 1 if not ( duration % len(code) == 0 ) else int(duration / len(code))
        code = code[:duration]
        
        if m not in code:
            continue
            
        if answer == "" or answer[0] < duration or (answer[0] == duration and answer[1] > start):
                answer = (duration, start, title)
                
    return answer[-1] if answer else "(None)"
