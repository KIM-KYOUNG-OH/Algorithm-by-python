def solution(s):
    answer = ''
    alps = ['z', 'o', 't', 'f', 's', 'e', 'n']
    i = 0
    while True:
        if i >= len(s):
            break
        if s[i] in alps:
            if s[i] == 'z':
                answer += '0'
                i += 4
            elif s[i] == 'o':
                answer += '1'
                i += 3
            elif s[i] == 't' and s[i+1] == 'w':
                answer += '2'
                i += 3
            elif s[i] == 't' and s[i+1] == 'h':
                answer += '3'
                i += 5
            elif s[i] == 'f' and s[i+1] == 'o':
                answer += '4'
                i += 4
            elif s[i] == 'f' and s[i+1] == 'i':
                answer += '5'
                i += 4
            elif s[i] == 's' and s[i+1] == 'i':
                answer += '6'
                i += 3
            elif s[i] == 's' and s[i+1] == 'e':
                answer += '7'
                i += 5
            elif s[i] == 'e':
                answer += '8'
                i += 5
            elif s[i] == 'n':
                answer += '9'
                i += 4
            continue
        answer += s[i]
        i += 1

    return int(answer)