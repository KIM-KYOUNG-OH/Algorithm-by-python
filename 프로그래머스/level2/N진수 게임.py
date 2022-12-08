def parse_notation(n, ch, cur):
    if cur == 0:
        return '0'
    result = ''
    while cur != 0:
        share = cur // n
        remainder = cur % n
        result = ch[remainder] + result
        cur = share
    return result


def solution(n, t, m, p):
    arr = []
    ch = [str(i) for i in range(10)]
    ch.extend([chr(i + 65) for i in range(6)])
    cur = 0
    while len(arr) < m * t:
        parsed_num = parse_notation(n, ch, cur)
        for i in range(len(parsed_num)):
            arr.append(parsed_num[i])
        cur += 1
    answer = []
    idx = (p - 1) - m
    while len(answer) < t:
        idx += m
        answer.append(arr[idx])
    return ''.join(answer)


solution(16, 16, 2, 1)