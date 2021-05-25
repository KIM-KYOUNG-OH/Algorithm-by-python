import sys


def binary_search():
    global answer
    left = 1
    right = max(lines)
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        for line in lines:
            cnt += line // mid
        if cnt >= n:
            answer = max(answer, mid)
            left = mid + 1
            continue
        if cnt < n:
            right = mid - 1
            continue


k, n = map(int, sys.stdin.readline().rstrip().split())
lines = []
for _ in range(k):
    lines.append(int(sys.stdin.readline().rstrip()))
answer = 0
binary_search()
print(answer)