import sys

n = int(sys.stdin.readline().rstrip())
people = []
for _ in range(n):
    name, korean, english, math = list(sys.stdin.readline().rstrip().split())
    people.append((name, int(korean), int(english), int(math)))
people.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in people:
    print(i[0])