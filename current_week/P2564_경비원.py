import sys


def get_distance(direct, size):
    if direct == 1:
        return size
    elif direct == 4:
        return wide + size
    elif direct == 2:
        return wide * 2 + height - size
    else:
        return (wide + height) * 2 - size


wide, height = map(int, sys.stdin.readline().rstrip().split())
n = int(input())
dist = []
cycle = (wide + height) * 2
for _ in range(n+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    dist.append(get_distance(a, b))
current = dist[-1]
answer = 0
for i in range(n):
    clockwise = abs(current - dist[i])
    rev_clockwise = cycle - clockwise
    answer += min(clockwise, rev_clockwise)
print(answer)