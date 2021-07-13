import sys

lst = list(map(int, list(sys.stdin.readline().rstrip())))
length = len(lst)
dp = [0] * (length + 1)
if lst[0] == 0:
    print(0)
    exit(0)
lst = [0] + lst  # 인덱싱을 위한 0
dp[0], dp[1] = 1, 1  # 초기값
for i in range(2, length + 1):
    cur = lst[i]  # 마지막 수가 한자리 수 일 때
    cur2 = lst[i - 1] * 10 + lst[i]  # 마지막 수가 두자리 수 일 때
    if 1 <= cur <= 9:  # 한자리수 가 성립할 때
        dp[i] += dp[i - 1]
    if 10 <= cur2 <= 26:  # 두 자리수가 성립할 때
        dp[i] += dp[i - 2]
    dp[i] %= 1000000
print(dp[-1])
