def solution(n, money):
    dp = [1] + [0] * n
    for coin in money:
        for price in range(coin, n + 1):
            dp[price] += dp[price - coin]
    return dp[n]


print(solution(5, [1, 2, 5]))
