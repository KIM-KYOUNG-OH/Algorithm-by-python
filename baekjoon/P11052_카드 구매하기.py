import sys

n = int(sys.stdin.readline().rstrip())
card_prices = [0]
card_prices.extend(list(map(int, sys.stdin.readline().rstrip().split())))
dp = [0] * (n + 1)
dp[1] = card_prices[1]
if n > 1:
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + card_prices[i - j])
print(dp[-1])
