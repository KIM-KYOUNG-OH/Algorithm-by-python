n, k = map(int, input().split())
cnt = 0
prime = [True] * (n+1)
prime[0], prime[1] = False, False
for i in range(2, n+1):
    if prime[i]:
        for j in range(i, n+1, i):
            if prime[j]:
                prime[j] = False
                cnt += 1
                if cnt == k:
                    print(j)
                    exit(0)