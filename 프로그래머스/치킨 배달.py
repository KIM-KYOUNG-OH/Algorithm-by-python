from itertools import combinations

n, m = map(int, input().split())
chickens = []
houses = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            houses.append((i, j))
        elif data[j] == 2:
            chickens.append((i, j))

candidates = list(combinations(chickens, m))


def get_total_chicken_distance(candidate):
    result = 0
    for house in houses:
        hx, hy = house
        chicken_distance = int(1e9)
        for cx, cy in candidate:
            distance = abs(cx - hx) + abs(cy - hy)
            chicken_distance = min(chicken_distance, distance)
        result += chicken_distance
    return result


answer = int(1e9)
for candidate in candidates:
    answer = min(answer, get_total_chicken_distance(candidate))
print(answer)