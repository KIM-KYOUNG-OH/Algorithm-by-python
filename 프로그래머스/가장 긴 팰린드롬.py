def solution(s):
    for i in range(len(s), 1, -1):
        a = i//2
        for j in range(len(s) + 1 - i):
            left = s[j:j + a]
            if i % 2:  # 홀수
                right = s[j + a + 1:j + a * 2 + 1]
            else:  # 짝수
                right = s[j + a:j + a * 2]
            if left == right[::-1]:
                return i
    return 1

print(solution("abcdefg"))