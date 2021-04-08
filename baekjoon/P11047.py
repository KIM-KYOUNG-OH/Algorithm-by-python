n,k = map(int, input().split())
lst = []
ans = 0
for _ in range(n):
    coin = int(input())
    if coin>k:
        continue
    lst.append(coin)
lst.sort(reverse=True)
for coin in lst:
    ans += k//coin
    if k%coin == 0:
        break
    k = k-coin*(k//coin)
print(ans)