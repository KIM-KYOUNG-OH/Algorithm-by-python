n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
temp = []

def recursive():
    if len(temp) == m:
        print(" ".join(map(str, temp)))
    for i in range(n):
        if lst[i] not in temp:
            temp.append(lst[i])
            recursive()
            temp.pop()

recursive()