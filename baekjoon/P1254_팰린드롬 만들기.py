import sys

s = sys.stdin.readline().rstrip()
l = len(s)
answer = 0
for i in range(l, l * 2):
    # print('i = ', i)
    mid = i // 2
    left = list(s[:mid])
    right = []
    if i % 2 == 0:
        right = list(s[mid:])
    else:
        right = list(s[mid + 1:])

    # print('left = ', left)
    # print('right = ', right)
    isPossible = True
    for e in right:
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
