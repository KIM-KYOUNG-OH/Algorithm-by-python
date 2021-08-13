def solution(money):
    # 첫 집은 털고 마지막 집은 안터는 경우
    dp1 = [0] * len(money)
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 2] + money[i], dp1[i - 1])
    max_dp1 = max(dp1)

    # 마지막 집은 털고 첫 집은 안터는 경우
    dp2 = [0] * len(money)
    dp2[-1], dp2[-2] = money[-1], max(money[-1], money[-2])
    for i in range(len(money) - 3, 0, -1):
        dp2[i] = max(dp2[i + 2] + money[i], dp2[i + 1])
    max_dp2 = max(dp2)

    return max(max_dp1, max_dp2)


print(solution([1, 2, 3]))