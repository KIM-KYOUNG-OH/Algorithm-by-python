import sys

s = sys.stdin.readline().rstrip()
l = len(s)
candidates = set()
for i in range(l):
    for j in range(i + 1, l + 1):
        candidates.add(s[i:j])
print(len(candidates))