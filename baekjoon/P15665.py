n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
temp = []
answer = set()


def recursive():
    if len(temp) == m:
        s = " ".join(map(str, temp))
        if s not in temp:
            answer.add(s)
        return
    for i in range(n):
        temp.append(lst[i])
        recursive()
        temp.pop()


recursive()
answer = sorted(list(answer))
for i in answer:
    print(i)