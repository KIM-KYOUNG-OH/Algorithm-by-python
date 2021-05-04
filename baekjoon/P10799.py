bar_razor = input()
answer = 0
stack = []
for i in range(len(bar_razor)):
    if bar_razor[i] == '(':
        stack.append('(')
    else:
        if bar_razor[i - 1] == '(':  # 레이저
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1  # 쇠막대기의 끄트머리 더함
print(answer)