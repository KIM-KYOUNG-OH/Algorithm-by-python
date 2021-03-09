def solution(number, k):
    stack = []
    for i in number:
        while stack and i > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)

    if k > 0:
        for _ in range(k):
            stack.pop()

    return "".join(stack)

print(solution("4177252841",4))