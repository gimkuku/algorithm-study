from datetime import datetime


def solution(m, musicinfos):
    answer = "(None)"
    maxcnt = -1

    m = (
        m.replace("A#", "a")
        .replace("C#", "c")
        .replace("D#", "d")
        .replace("F#", "f")
        .replace("G#", "g")
    )

    for info in musicinfos:
        start, end, name, melody = info.split(",")

        melody = (
            melody.replace("A#", "a")
            .replace("C#", "c")
            .replace("D#", "d")
            .replace("F#", "f")
            .replace("G#", "g")
        )

        start = datetime.strptime(start, "%H:%M")
        end = datetime.strptime(end, "%H:%M")

        playtime = (end - start).seconds // 60

        melody *= (playtime // len(melody)) + 1
        melody = melody[:playtime]

        if m in melody:
            if maxcnt < playtime:
                answer = name
                maxcnt = playtime

    return answer


solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
