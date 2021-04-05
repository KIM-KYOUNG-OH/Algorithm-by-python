def solution(a):
    answer = [False] * len(a)
    left_min, right_min = 10**9+1, 10**9+1
    for i in range(len(a)):
        if a[i]<left_min:
            answer[i] = True
            left_min = a[i]
        if a[-1-i]<right_min:
            answer[-1-i] = True
            right_min = a[-1-i]

    return sum(answer)

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))