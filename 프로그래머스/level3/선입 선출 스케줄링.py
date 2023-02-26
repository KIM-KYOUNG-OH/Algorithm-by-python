def solution(n, cores):
    if n <= len(cores):
        return n

    left = 1
    right = min(cores) * n

    while left < right:
        mid = (left + right) // 2
        capacity = 0
        for c in cores:
            capacity += mid // c + 1
        if capacity >= n:
            right = mid
        else:
            left = mid + 1

    for c in cores:
        n -= (right - 1) // c + 1

    for i in range(len(cores)):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1


print(solution(6, [1, 2, 3]))

