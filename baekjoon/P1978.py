n = int(input())
lst = list(map(int, input().split()))
ans = 0
def is_decimal(n):
    if n==1:
        return False
    elif n==2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

for num in lst:
    if is_decimal(num):
        ans+=1
print(ans)