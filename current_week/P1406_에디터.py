import sys

left = list(sys.stdin.readline().rstrip())
right = []
m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    order = list(sys.stdin.readline().rstrip().split())
    if order[0] == 'L':
        if len(left) == 0:
            continue
        right.append(left.pop())
        continue
    if order[0] == 'D':
        if len(right) == 0:
            continue
        left.append(right.pop())
        continue
    if order[0] == 'B':
        if len(left) == 0:
            continue
        left.pop()
        continue
    if order[0] == 'P':
        left.append(order[1])
print(''.join(left + list(reversed(right))))

