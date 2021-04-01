def recursive():
    if len(temp) == m:
        print(" ".join(map(str, temp)))
    for i in range(len(lst)):
        if lst[i] not in temp:
            temp.append(lst[i])
            recursive()
            temp.pop()

n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
temp = []
recursive()
