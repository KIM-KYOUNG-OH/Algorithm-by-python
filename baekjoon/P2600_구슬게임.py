import sys

d = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0] * 501
for i in range(1, 501):
    check = set()
    for j in d:
        if i - j >= 0:
            check.add(dp[i - j])

    gnum = 0
    while gnum in check:
        gnum += 1
    dp[i] = gnum

for _ in range(5):
    k1, k2 = map(int, sys.stdin.readline().rstrip().split())
    if dp[k1] ^ dp[k2] > 0:
        print('A')
    else:
        print('B')

