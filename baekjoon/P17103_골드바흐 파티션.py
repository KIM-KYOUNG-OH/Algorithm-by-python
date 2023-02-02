import sys

t = int(sys.stdin.readline().rstrip())
cases = []
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    cases.append(n)
max_val = max(cases)
prime = [True] * (max_val + 1)
prime[0], prime[1] = False, False
for i in range(2, int(max_val ** 0.5) + 1):
    for j in range(i + i, max_val + 1, i):
        prime[j] = False

answer = []
for n in cases:
    cnt = 0
    for i in range(2, n // 2 + 1):
        j = n - i
        if prime[i] and prime[j]:
            cnt += 1
    answer.append(cnt)

for a in answer:
    print(a)