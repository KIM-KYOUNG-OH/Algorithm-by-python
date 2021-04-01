n, m = map(int, input().split())
lst = [i for i in range(1, n + 1)]
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
