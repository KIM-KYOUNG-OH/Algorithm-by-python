import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dictionary1 = dict()
dictionary2 = dict()
question = []
for i in range(1, n + 1):
    name = sys.stdin.readline().rstrip()
    dictionary1[i] = name
    dictionary2[name] = i
for _ in range(m):
    question.append(sys.stdin.readline().rstrip())
for q in question:
    if q.isalpha():
        print(dictionary2[q])
        continue
    if q.isdecimal():
        print(dictionary1[int(q)])
