def solution(name):
    change = [min(ord(i)-ord("A"), ord("Z")-ord(i)+1) for i in list(name)]
    answer = 0
    idx = 0
    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0:
            break
        left, right = 1, 1
        while change[idx-left] == 0:
            left += 1
        while change[idx+right] == 0:
            right += 1
        answer += left if left<right else right
        idx += -left if left<right else right

    return answer

print(solution("JEROEN"))