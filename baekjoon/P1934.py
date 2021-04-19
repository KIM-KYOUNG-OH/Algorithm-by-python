n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    if a < b:
        a, b = b, a
    i = 1
    while True:
        if (a*i)%b == 0:
            print(a * i)
            break
        else:
            i += 1
