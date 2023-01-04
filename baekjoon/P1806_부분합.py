import sys

n, s = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
csum = lst[0]
i, j = 0, 0
answer = sys.maxsize
while True:
    if csum >= s:
        answer = min(answer, j - i + 1)
        csum -= lst[i]
        i += 1
    else:
        j += 1
        if j == n:
            break
        csum += lst[j]
if answer == sys.maxsize:
    print(0)
else:
    print(answer)