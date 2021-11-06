import sys

is_prime = [True] * 1000001
is_prime[0], is_prime[1] = False, False
for i in range(2, int(1000000 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i + i, 1000001, i):
            is_prime[j] = False

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    breaker = False
    for i in range(3, n // 2 + 1, 2):
        if is_prime[i] and is_prime[n - i]:
            print(n, '=', i, '+', n - i)
            breaker = True
            break
    if breaker:
        continue
    print("Goldbach's conjecture is wrong.")
