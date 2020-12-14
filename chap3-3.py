n, m = map(int, input().split())
result = 0
for _ in range(n):
    lst = list(map(int, input().split()))
    lst.sort()
    if result < lst[0]:
        result = lst[0]
print(result)
