import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
not_heard = set()
not_seen = set()
for _ in range(n):
    not_heard.add(sys.stdin.readline().rstrip())
for _ in range(m):
    not_seen.add(sys.stdin.readline().rstrip())
answer = list(not_heard & not_seen)
print(len(answer))
answer.sort()
for data in answer:
    print(data)
