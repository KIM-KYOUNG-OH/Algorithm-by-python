import sys

n = int(sys.stdin.readline().rstrip())
total = 1
answer = 0
start, end = 1, 1
while start <= n:
    if total < n:
        end += 1
        total += end
    elif total > n:
        total -= start
        start += 1
    else:
        # print(start, end)
        answer += 1
        total -= start
        start += 1
print(answer)
