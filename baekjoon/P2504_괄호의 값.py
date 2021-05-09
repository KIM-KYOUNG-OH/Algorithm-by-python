s = input()
stack = []
answer = 0
for ch in s:
    if ch == '(' or ch == '[':
        stack.append(ch)
        continue
    if ch == ')':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:   # temp != 0
                    stack.append(2 * temp)
                break
            if top == '[':  # 괄호 invalid
                print(0)
                exit(0)
            temp += int(top)
        continue
    if ch == ']':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            if top == '(':  # 괄호 invalid
                print(0)
                exit(0)
            temp += int(top)
        continue

for i in stack: # stack에 있는 수를 모두 더해준다
    if i == '(' or i == '[':    # 괄호 invalid
        print(0)
        exit(0)
    answer += i
print(answer)