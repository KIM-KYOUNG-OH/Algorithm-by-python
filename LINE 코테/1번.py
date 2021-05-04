def solution(inputString):
    answer = 0  # 정상적인 괄호 총 개수
    open_brackets = {'(': 0, '{': 0, '[': 0, '<': 0}  # 괄호모양: 개수
    closed_brackets = [')', '}', ']', '>']
    index = -1
    stack = []
    wrong = 0  # 비정상 괄호 index
    for alp in inputString:
        if alp == ' ':  # 공백은 건너뜀
            continue
        index += 1
        if index == 0 and alp in closed_brackets:  # 첫문자가 닫힌 괄호일때
            return 0
        if alp == ')':
            stack_top = stack.pop()
            if stack_top != '(':
                wrong = index * (-1)
            elif stack_top == '(':
                answer += 1
                open_brackets['('] -= 1
        elif alp == '}':
            stack_top = stack.pop()
            if stack_top != '{':
                wrong = index * (-1)
            elif stack_top == '{':
                answer += 1
                open_brackets['{'] -= 1
        elif alp == ']':
            stack_top = stack.pop()
            if stack_top != '[':
                wrong = index * (-1)
            elif stack_top == '[':
                answer += 1
                open_brackets['['] -= 1
        elif alp == '>':
            stack_top = stack.pop()
            if stack_top != '<':
                wrong = index * (-1)
            elif stack_top == '<':
                answer += 1
                open_brackets['<'] -= 1
        elif alp in list(open_brackets.keys()):
            open_brackets[alp] += 1
            stack.append(alp)
    if wrong != 0:
        return wrong
    if len(stack) != 0:
        return (index+1) * (-1)
    return answer

print(solution('line [({<plus>)}]'))