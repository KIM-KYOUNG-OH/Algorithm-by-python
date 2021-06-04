import sys

m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    order = sys.stdin.readline().rstrip().split()
    bit = 0
    if len(order) == 1:
        if order[0] == 'all':
            bit = (1 << 20) - 1
        else:
            bit = 0
        continue
    command = order[0]
    num = int(order[1]) - 1
    if command == 'add':
        bit |= (1 << num)
    elif command == 'remove':
        bit &= ~(1 << num)
    elif command == 'check':
        if bit & (1 << num) == 0:
            print(0)
        else:
            print(1)
    elif command == 'toggle':
        bit = bit ^ (1 << num)

