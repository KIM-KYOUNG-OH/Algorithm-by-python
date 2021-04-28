from collections import deque

n = int(input())
q = deque()
answer = 0
for i in range(1, n+1):
    q.appendleft(i)
while True:
    if len(q) == 1:
        answer = q[0]
        break
    q.pop()
    q.appendleft(q.pop())
print(answer)