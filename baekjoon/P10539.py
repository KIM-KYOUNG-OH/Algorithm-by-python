n= int(input())
lst = list(map(int, input().split()))

A=[lst[0]]

for i in range(1,n):
    A.append(lst[i]*(i+1)-sum(A))
for i in A:
    print(i, end=" ")