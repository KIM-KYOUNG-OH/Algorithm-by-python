import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = []  # 동전의 가치
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))
dp = [-1] * (k + 1)  # 초기화
dp[0] = 0  # 초기값
for i in range(1, k + 1):
    for j in range(n):
        if coins[j] <= i and dp[i - coins[j]] != -1:
            if dp[i] == -1:  # dp에 처음 입력할 때
                dp[i] = dp[i - coins[j]] + 1
            elif dp[i] != -1:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)  # (dp[i - coins[j]] + 1)의 최소값을 dp[i]에 저장
print(dp[-1])
