import sys

while True:
    s = sys.stdin.readline().rstrip()
    stack = []
    true_flag = True
    if s == '.':
        break
    for alp in s:
        if alp == '(' or alp == '[':
            stack.append(alp)
            continue
        if alp == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                true_flag = False
                break
        if alp == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                true_flag = False
                break
    if true_flag and len(stack) == 0:
        print('yes')
    else:
        print('no')

