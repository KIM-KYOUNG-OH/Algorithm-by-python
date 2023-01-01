def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left = 0
    right = distance
    while left <= right:
        delCnt = 0
        preRock = 0
        mid = (left + right) // 2
        for rock in rocks:
            if rock - preRock < mid:
                delCnt += 1
            else:
                preRock = rock
            if delCnt > n:
                break
        if delCnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))