from itertools import combinations


def solution():
    ans = int(1e9)
    for candidiate in combinations(people, n // 2):
        start_member = list(candidiate)
        link_member = list(set(people) - set(candidiate))

        comb_start = combinations(start_member, 2)
        comb_link = combinations(link_member, 2)

        start_sum = 0
        for x, y in comb_start:
            start_sum += matrix[x][y] + matrix[y][x]

        link_sum = 0
        for x, y in comb_link:
            link_sum += matrix[x][y] + matrix[y][x]

        diff = abs(start_sum - link_sum)
        if diff == 0:
            return 0
        ans = min(ans, diff)
    return ans


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
people = [i for i in range(n)]
print(solution())
