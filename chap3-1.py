n = int(input())
lst = [500, 100, 50, 10]
cnt = 0
for i in lst:
    if i <= n:
        cnt += (n // i)
        n %= i

print(cnt)