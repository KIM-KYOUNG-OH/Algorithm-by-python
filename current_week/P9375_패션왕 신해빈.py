import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    cloth = dict()
    for _ in range(n):
        cloth_name, kind = sys.stdin.readline().rstrip().split()
        if kind not in cloth:
            cloth[kind] = 1
            continue
        cloth[kind] += 1
    cloth_counts = cloth.values()
    answer = 1
    for i in cloth_counts:
        answer *= (i + 1)
    print(answer - 1)
