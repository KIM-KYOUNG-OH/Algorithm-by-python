n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
temp = []

def recursive(a):
    if len(temp) == m:
        print(" ".join(map(str, temp)))
        return
    for i in range(a, n):
        temp.append(lst[i])
        recursive(i)
        temp.pop()

recursive(0)