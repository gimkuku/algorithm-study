def get_play_time(start, end):
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    return (eh-sh)*60 + (em-sm)

def get_song_list(song):
    song_list = []
    for s in song:
        if s == '#':
            song_list[len(song_list) - 1] += '#'
        else:
            song_list.append(s)
    return song_list

def solution(m, musicinfos):
    answer = ''
    searched = []
    
    for info in musicinfos:
        start, end, title, song = info.split(",")
        play_time = get_play_time(start,end)
        
        song_list = get_song_list(song)
        m_list = get_song_list(m)

        song_len = len(song_list)
        m_len = len(m_list)
        
        played_song = []
        for _ in range(play_time//song_len):
            played_song += song_list
        for i in song_list[:play_time%song_len]:
            played_song.append(i)
        
        for i in range(play_time - m_len + 1):
            for j in range(m_len):
                if played_song[i+j] != m_list[j]:
                    break
            else:
                searched.append((play_time, title))
    
    max_play_time = 0
    for p, t in searched:
        if p > max_play_time:
            max_play_time = p
    
    for p, t in searched:
        if max_play_time == p:
            answer = t
            break
    return answer if answer != '' else "(None)"