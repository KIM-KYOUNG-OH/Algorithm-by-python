nums = [i for i in range(10001)]
visited = [False] * 10001

def dn(n):
    sum = n
    while n != 0:
        sum += n%10
        n = n//10
    if sum > 10000:
        return
    visited[sum] = True
    dn(sum)

for i in range(1, len(nums)):
    if visited[i] == False:
        print(i)
        dn(i)