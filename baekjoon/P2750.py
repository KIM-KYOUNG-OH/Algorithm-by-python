n = int(input())
arr = []
for _ in range (n):
    arr.append(int(input()))
for j in range(len(arr)-1):
    for i in range(len(arr)-1-j):
        if i == len(arr)-1:
            break
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
for i in arr:
    print(i)