n,m,k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
total = 0
cnt = 0
for i in range(m):
    if cnt < k:
        total += lst[n-1]
        cnt += 1
    else:
        total += lst[n-2]
        cnt = 0
print(total)