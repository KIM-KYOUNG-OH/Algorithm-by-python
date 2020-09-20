n = int(input())
arr = list()
for _ in range(n):
    data = list(input().split(" "))
    arr.append((int(data[0]), data[1]))
result = sorted(arr, key = lambda x : x[0])
for i in result:
    print(i[0], i[1])
