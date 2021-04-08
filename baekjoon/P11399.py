n = int(input())
lst = list(map(int, input().split()))
lst.sort()
dp = [0]*n
dp[0] = lst[0]
for i in range(1,n):
    dp[i] = dp[i-1] + lst[i]

sum = 0
for i in range(n):
    sum += dp[i]
print(sum)