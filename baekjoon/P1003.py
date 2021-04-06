n = int(input())
a = [1,0]
b = [0,1]
for i in range(2, 41):
    a.append(a[i-1] + a[i-2])
    b.append(b[i-1] + b[i-2])
for _ in range(n):
    num = int(input())
    print(' '.join(map(str, [a[num], b[num]])))