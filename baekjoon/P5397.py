test_case = int(input())
left_stack = []
right_stack = []
for _ in range(test_case):
    req = list(input())
    for i in range (len(req)):
        if req[i] == '<':          
            if (len(left_stack) != 0):
                right_stack.append(left_stack.pop())
            else:
                continue
        elif req[i] == '>':
            if (len(right_stack) != 0):
                left_stack.append(right_stack.pop())
            else:
                continue
        elif req[i] == '-':
            if(len(left_stack) != 0):
                left_stack.pop()
            else:
                continue
        else:
            left_stack.append(req[i])
    for _ in range (len(right_stack)):
        left_stack.append(right_stack.pop())
    for i in range (len(left_stack)):
        print(left_stack[i], end='')
    left_stack.clear()
    right_stack.clear()
    print()