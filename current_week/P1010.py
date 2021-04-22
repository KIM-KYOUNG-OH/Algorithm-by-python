def factorial(x):
    result = 1
    for i in range(2, x+1):
        result *= i
    return result


T = int(input())
for _ in range(T):
    n,m = map(int, input().split())
    ans = factorial(m) // (factorial(m-n) * factorial(n))
    print(ans)