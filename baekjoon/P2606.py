def bfs(lst, start):
    result = []
    visit = []
    queue = []
    visit = [False]*len(lst)
    visit[start] = True
    queue.append(start)
    while len(queue)>0:
        i = queue.pop(0)
        result.append(i)
        for j in lst[i]:
            if visit[j] == False:
                queue.append(j)
                visit[j]=True
    return result

node=int(input())
edge=int(input())
lst = [[] for i in range(node+1)]
for i in range(edge):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()
answer = bfs(lst,1)
print(len(answer)-1)