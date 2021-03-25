def solution(s):
    start, end = 0,0
    d = dict()
    for i in range(1, len(s)-1):
        if s[i] == "{":
            start = i+1
        elif s[i] == "}":
            end = i
            lst = list(map(int, s[start:end].split(",")))
            for n in lst:
                if n not in d.keys():
                    d[n] = 1
                else:
                    d[n] += 1
    d = sorted(d.items(), key=lambda x:-x[1])
    return [idx for idx, value in d]

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))