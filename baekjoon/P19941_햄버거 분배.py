import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
pos = sys.stdin.readline().rstrip()
visit = [False] * n
answer = 0
for i in range(n):
    if pos[i] == 'H':
        continue
    for j in range(i - k, i + k + 1):
        if j >= n:
            break
        elif j < 0:
            continue
        elif j == i:
            continue

        if pos[j] == 'H' and not visit[j]:
            visit[j] = True
            answer += 1
            break
print(answer)
