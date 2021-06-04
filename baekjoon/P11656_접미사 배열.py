import sys

s = sys.stdin.readline().rstrip()
lst = []
for i in range(len(s)):
    lst.append(s[i:])
lst.sort()
for i in lst:
    print(i)