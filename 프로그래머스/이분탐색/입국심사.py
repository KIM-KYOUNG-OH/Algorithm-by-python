def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left <= right:
        count = 0
        mid = (left + right) // 2
        for time in times:
            count += mid // time
            if count >= n:
                break
        if count >= n:
            answer = mid
            right = mid - 1
        elif count < n:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))