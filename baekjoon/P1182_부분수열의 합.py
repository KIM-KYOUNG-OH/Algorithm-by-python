import sys


def recursive(idx, total):
    global answer
    if idx >= n:
        return
    total += numbers[idx]
    if total == s:
        answer += 1
    recursive(idx + 1, total - numbers[idx])
    recursive(idx + 1, total)


n, s = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0
recursive(0, 0)
print(answer)