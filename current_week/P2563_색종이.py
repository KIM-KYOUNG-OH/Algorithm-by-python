import sys

n = int(sys.stdin.readline().rstrip())
answer = 0
paper = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            paper[i][j] = 1
for row in paper:
    answer += row.count(1)
print(answer)
