n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
temp = []
visited = [False] * n
answer = []


def recursive(a):
    if len(temp) == m:
        s = " ".join(map(str, temp))
        if s not in answer:
            answer.append(s)
        return
    for i in range(a, n):
        if not visited[i]:
            temp.append(lst[i])
            visited[i] = True
            recursive(i+1)
            temp.pop()
            visited[i] = False


recursive(0)
for i in answer:
    print(i)