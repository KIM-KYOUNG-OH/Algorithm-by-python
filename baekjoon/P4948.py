request = []
while True:
    n = int(input())
    if n == 0:
        break
    request.append(n)
prime = [True] * (max(request) * 2 + 1)
prime[0], prime[1] = False, False

for i in range(2, int((max(request)*2) ** 0.5) + 1):
    if not prime[i]:
        continue
    j = 2
    while True:
        if i * j > (len(prime) - 1):
            break
        prime[i * j] = False
        j += 1

for num in request:
    cnt = 0
    for i in range(num + 1, num * 2 + 1):
        if prime[i]:
            cnt += 1
    print(cnt)