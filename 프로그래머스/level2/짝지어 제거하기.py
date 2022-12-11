from collections import deque


def solution(s):
    stack = deque()
    for ch in s:
        if len(stack) == 0:
            stack.append(ch)
        else:
            if stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

    if len(stack) > 0:
        return 0
    else:
        return 1


print(solution('baabaa'))
