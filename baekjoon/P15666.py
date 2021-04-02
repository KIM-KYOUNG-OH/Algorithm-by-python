n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
temp = []
answer = []

def recursive(a):
    if len(temp) == m:
        s = " ".join(map(str, temp))
        if s not in answer:
            answer.append(s)
            print(s)
        return
    for i in range(a, n):
        temp.append(lst[i])
        recursive(i)
        temp.pop()

recursive(0)