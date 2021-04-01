n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
temp = []
visited = [False] * n
answer = set()


def recursive():
    if len(temp) == m:
        answer.add(tuple(temp))
        return
    for i in range(n):
        if not visited[i]:
            temp.append(lst[i])
            visited[i] = True
            recursive()
            temp.pop()
            visited[i] = False


recursive()
answer = sorted(list(answer))
for i in answer:
    print(" ".join(map(str, i)))
