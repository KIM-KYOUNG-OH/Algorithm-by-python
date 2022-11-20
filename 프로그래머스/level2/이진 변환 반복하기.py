def solution(s):
    return recursive(s)


def recursive(s):
    convert_cnt, zero_cnt = 0, 0
    while True:
        if s == '1':
            answer = [convert_cnt, zero_cnt]
            return answer
        zero = 0
        for ch in list(s):
            if ch == '0':
                zero += 1

        fixed_s = s.replace('0', '')
        convert_cnt += 1
        zero_cnt += zero
        s = bin(len(fixed_s))[2:]


solution("110010101001")