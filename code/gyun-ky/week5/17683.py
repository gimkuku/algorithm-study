
def full_music(minfo):
    st, et, t, music_part = minfo.split(',')
    
    music_part = parse_music(music_part)
    
    sh, sm = map(int, st.split(':'))
    eh, em = map(int, et.split(':'))
    
    play_time = (eh*60 + em) - (sh*60 + sm)
    
    if play_time < len(music_part):
        full_music = music_part[0:play_time]
    else:
        iter_time = play_time // (len(music_part))
        last_time = play_time % (len(music_part))
        print(iter_time)
        print(last_time)
        full_music = music_part*iter_time + music_part[0:last_time]
    
    return (t, play_time, full_music)


def parse_music(m_str):
    result = m_str.replace('C#', 'c')
    result = result.replace('D#', 'd')
    result = result.replace('F#', 'f')
    result = result.replace('G#', 'g')
    result = result.replace('A#', 'a')
            
    return result
    


def solution(m, musicinfos):

    m = parse_music(m)
    print(m)
    
    max_play_time = -1
    answer = '(None)'
    for minfo in musicinfos:
        title, play_time, music = full_music(minfo)
        print(f'play_time : {play_time}')
        print(f'music : {music}')
        if m in music:
            if max_play_time < play_time:
                answer = title
                max_play_time = play_time
    

    return answer