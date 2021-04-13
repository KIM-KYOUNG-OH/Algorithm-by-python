m = int(input())
n = int(input())
prime = [True] * (n+1)
prime[1] = False # 1은 소수가 아니다
lst = []
for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        for j in range(i+i, n+1, i):
            prime[j] = False
for i in range(m, n+1):
    if prime[i]:
        lst.append(i)
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])