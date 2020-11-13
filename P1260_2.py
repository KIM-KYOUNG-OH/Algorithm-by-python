from collections import deque
import sys

def process(n,m):
    lst = [[] for i in range(n+1)]
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        lst[a].append(b)
        lst[b].append(a)
    for i in lst:
        i.sort()
    return lst

def dfs(lst,start):
    visit = [False for i in range(len(lst))]
    stack = list()
    result = list()
    stack.append(start)
    while len(stack)>0:
        i = stack.pop()
        if visit[i] == False:
            result.append(i)
            visit[i]=True
            for j in reversed(lst[i]):
                stack.append(j)
    return result

def bfs(lst,start):
    visit = [False for i in range(len(lst))]
    queue = deque()
    queue.append(start)
    visit[start]=True
    result = []
    while len(queue)>0:
        i = queue.popleft()
        result.append(i)
        for j in lst[i]:
            if visit[j] == False:
                queue.append(j)
                visit[j] = True
    return result

n, m, v = map(int, sys.stdin.readline().split())
lst = process(n,m)
result = dfs(lst,v)
for i in result:
    print(i, end=' ')
print()
result = bfs(lst,v)
for i in result:
    print(i, end=' ')