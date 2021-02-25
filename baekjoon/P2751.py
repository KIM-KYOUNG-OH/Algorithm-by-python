n = int(input())
array=list()
for _ in range(n):
    array.append(int(input()))
result=sorted(array, reverse=False)
for data in result:
    print(data)