import sys

n = int(sys.stdin.readline().rstrip())
if n < 3:
    max_val = 3
else:
    max_val = n
isPrime = [True] * (max_val + 1)
isPrime[0], isPrime[1] = False, False
for i in range(2, int(max_val ** 0.5) + 1):
    for j in range(i + i, max_val + 1, i):
        isPrime[j] = False
primes = []
for i in range(2, n + 1):
    if isPrime[i]:
        primes.append(i)

answer = 0
left, right = 0, 0
while left <= right <= len(primes):
    # print('left = ', left, ', right = ', right)
    candidate = primes[left:right]
    total = sum(candidate)
    if total < n:
        right += 1
    elif total == n:
        # print('hit')
        answer += 1
        left += 1
    else:
        left += 1
print(answer)
