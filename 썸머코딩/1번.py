def solution(code, day, data):
    answer = []
    result = []
    for dat in data:
        dat = list(dat.split())
        if dat[1][5:] == code:
            if dat[2][5:13] == day:
                result.append((int(dat[0][6:]), int(dat[2][5:])))  # (price, time)
    result.sort(key=lambda x: x[1])
    for i in result:
        answer.append(i[0])

    return answer

print(solution())