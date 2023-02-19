from collections import deque, defaultdict


def parseMinute(time):
    time = time.split(':')
    result = 60 * int(time[0]) + int(time[1])
    return result


def parseToStr(answer):
    share = answer // 60
    remainder = answer % 60
    return str(share).rjust(2, '0') + ':' + str(remainder).rjust(2, '0')


def solution(n, t, m, timetable):
    bus_stop = []
    for i in range(9 * 60, 24 * 60, t):
        if n == 0:
            break
        bus_stop.append(i)
        n -= 1
    boarding = defaultdict(list)

    fixed_timetable = []
    for time in timetable:
        tmp = parseMinute(time)
        fixed_timetable.append(tmp)
    q = deque(sorted(fixed_timetable))

    for i in range(len(bus_stop)):
        bus_come = bus_stop[i]
        while len(boarding[bus_come]) < m:
            if len(q) == 0:
                break
            if q[0] > bus_come:
                break
            person = q.popleft()
            boarding[bus_come].append(person)

    answer = 0
    if len(boarding[bus_stop[-1]]) == m:
        answer = boarding[bus_stop[-1]][-1] - 1
    else:
        answer = bus_stop[-1]
    return parseToStr(answer)


print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))