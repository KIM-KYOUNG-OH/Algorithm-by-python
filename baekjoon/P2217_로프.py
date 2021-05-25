import sys

n = int(sys.stdin.readline().rstrip())
ropes = []
for _ in range(n):
    ropes.append(int(sys.stdin.readline().rstrip()))
ropes.sort(reverse=True)
possible_weights = []
for i in range(len(ropes)):
    possible_weights.append(ropes[i] * (i + 1))
print(max(possible_weights))
