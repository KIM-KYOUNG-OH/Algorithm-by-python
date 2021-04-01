n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
temp = []

def recursive():
    if len(temp) == m:
        print(" ".join(map(str, temp)))
        return
    for i in range(n):
        temp.append(lst[i])
        recursive()
        temp.pop()

recursive()