def recursive(a):
    if len(temp) == m:
        print(" ".join(map(str, temp)))
    for i in range(a, n):
        temp.append(lst[i])
        recursive(i+1)
        temp.pop()

n,m = map(int, input().split())
lst = [i for i in range(1, n+1)]
temp = []
recursive(0)