n = int(input())
A = list(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))
for i in lst:
    if i in A:
        print(1)
    else:
        print(0)