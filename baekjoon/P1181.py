n = int(input())
lst = set(input() for _ in range(n))
s = [(len(i), i) for i in lst]
s.sort(key=lambda x: (x[0], x[1]))
for i in s:
    print(i[1])
