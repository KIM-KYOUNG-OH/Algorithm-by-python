import sys

lst = list(map(int, list(sys.stdin.readline().rstrip())))
length = len(lst)
dp = [0] * (length + 1)
if lst[0] == 0:
    print(0)
    exit(0)
lst = [0] + lst
dp[0], dp[1] = 1, 1
for i in range(2, length + 1):
    cur = lst[i]
    cur2 = lst[i - 1] * 10 + lst[i]
    if 1 <= cur <= 9:
        dp[i] += dp[i - 1]
    if 10 <= cur2 <= 26:
        dp[i] += dp[i - 2]
    dp[i] %= 1000000
print(dp[1])
