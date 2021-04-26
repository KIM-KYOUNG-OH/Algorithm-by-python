n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
ans = 0
for i in matrix:
    ans = max(ans, min(i))
print(ans)