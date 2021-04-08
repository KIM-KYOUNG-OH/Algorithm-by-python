m,n = map(int, input().split())
# 에라토스테네스의 체 : 소수가 아닌 숫자를 지워나가면서 소수를 찾는 방법
prime = [True] * (n+1)
prime[0], prime[1] = False, False
# n의 제곱근까지만 방문
for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        for j in range(2*i, n+1, i):
            prime[j] = False
for i in range(m, n+1):
    if prime[i]:
        print(i)