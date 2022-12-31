def solution(n, times):
    left = 0
    right = min(times) * n
    while left < right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt < n:
            left = mid + 1
        else:
            right = mid
    return right


print(solution(6, [7, 10]))
