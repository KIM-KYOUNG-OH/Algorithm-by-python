import sys

s = sys.stdin.readline().rstrip()
l = len(s)
answer = 0
for i in range(l + 1, l * 2):
    left, right = [], []
    if i % 2 == 0:
        left = list(s[:i])
        right = s[i:]
    else:
        left = list(s[:i])
        right = s[i + 1:]

    isPossible = True
    for e in right[::-1]:
        cur = left.pop()
        if cur != e:
            isPossible = False
            break

    if isPossible:
        answer = i
        break
if answer == 0:
    print(l * 2)
else:
    print(answer)
