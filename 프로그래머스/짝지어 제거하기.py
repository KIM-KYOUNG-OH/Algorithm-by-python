def solution(s):
    stack = []
    for alp in s:
        if not stack:
            stack.append(alp)
        elif alp == stack[-1]:
            stack.pop()
        else:
            stack.append(alp)
    if not stack:
        return 1
    else:
        return 0


print(solution('aaaba'))