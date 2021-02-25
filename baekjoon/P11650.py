n = int(input())
arr = list()
for _ in range(n):
    x, y = map(int, input().split(" "))
    arr.append((x, y))
result = sorted(arr)
for i in result:
    print(i[0], i[1])