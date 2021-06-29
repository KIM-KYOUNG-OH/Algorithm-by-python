import sys

prime = [True] * 10001
prime[0], prime[1] = False, False
for i in range(2, int((10000 ** 0.5)) + 1):
    for j in range(i * 2, 10001, i):
        prime[j] = False
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    for i in range(n // 2, 1, -1):
        if prime[n - i] and prime[i]:
            print(i, n - i)
            break
