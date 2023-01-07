import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
visited = [False] * n
idx = 0
answer = []
while True:
    move = lst[idx]
    visited[idx] = True
    answer.append(idx + 1)
    if len(answer) >= len(lst):
        break
    if move > 0:
        while True:
            if move == 0:
                break
            idx += 1
            if idx >= len(lst):
                idx = 0
            if not visited[idx]:
                move -= 1
    else:
        while True:
            if move == 0:
                break
            idx -= 1
            if not visited[idx]:
                move += 1
            if idx < 0:
                idx += len(lst)
print(' '.join(map(str, answer)))
