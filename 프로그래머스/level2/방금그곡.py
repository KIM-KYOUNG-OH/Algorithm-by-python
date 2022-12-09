import math


def solution(m, musicinfos):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    answer = None
    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(',')
        hour, sec = map(int, start.split(':'))
        start_time = hour * 60 + sec
        hour, sec = map(int, end.split(':'))
        end_time = hour * 60 + sec
        duration = end_time - start_time
        code = code.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        code *= math.ceil(duration / len(code))
        code = code[:duration]

        if m not in code:
            continue

        if answer is None or duration > answer[0]:
            answer = (duration, title)

    if answer is None:
        return '(None)'
    else:
        return answer[1]


solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
