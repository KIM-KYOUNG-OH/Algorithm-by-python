import sys
n = int(sys.stdin.readline())
arr = [0] * 10001
for _ in range(n):
    data = int(sys.stdin.readline())
    arr[data] += 1
for i in range(10001):
    if arr[i] != None:
        for _ in range(arr[i]):
            print(i)
