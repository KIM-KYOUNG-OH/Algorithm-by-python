n,m,k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
cnt = 0
for _ in range(m):
    if cnt >= k:
        ans += arr[-2]
        cnt = 0
    else:
        ans += arr[-1]
        cnt += 1
print(ans)