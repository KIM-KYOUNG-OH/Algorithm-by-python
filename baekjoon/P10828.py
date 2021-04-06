import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    order = sys.stdin.readline().split()
    ord = order[0]
    if ord == 'push':
        stack.append(int(order[1]))
    elif ord == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif ord == 'size':
        print(len(stack))
    elif ord == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif ord == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])