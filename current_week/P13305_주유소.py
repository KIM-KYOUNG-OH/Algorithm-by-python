import sys

n = int(sys.stdin.readline().rstrip())
roads = list(map(int, sys.stdin.readline().rstrip().split()))
costs = list(map(int, sys.stdin.readline().rstrip().split()))
total = 0
min_cost = int(1e9)

for i in range(n - 1):
    if i == 0:
        min_cost = min(min_cost, costs[i])
        total += costs[0] * roads[0]
    else:
        min_cost = min(min_cost, costs[i])
        total += min_cost * roads[i]
print(total)
