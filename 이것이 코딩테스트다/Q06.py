def solution(food_times, k):
    left, right = 0, int(1e8)
    n, cutting, idx = len(food_times), 0, 0
    while left <= right:
        mid = (left+right)//2
        v = n*mid
        for i in food_times:
            if (i-mid) < 0:
                v += (i-mid)
        if v <= k:
            cutting, idx = mid, v
            left = mid+1
        else:
            right = mid -1
    food_times = [t-cutting for t in food_times]
    for i in range(n):
        if food_times[i] > 0 and idx == k:
            return i + 1
        else:
            if food_times[i] > 0:
                idx += 1
    return -1


print(solution([3, 1, 2], 5))