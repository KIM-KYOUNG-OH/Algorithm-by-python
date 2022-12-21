def solution(s):
    stack = []
    for ch in s:
        if len(stack) == 0:
            stack.append(ch)
        else:
            if ch == '(':
                stack.append(ch)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
    if len(stack) > 0:
        return False
    return True
