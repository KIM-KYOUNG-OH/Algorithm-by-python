def solution(number, k):
    stack = []
    for e in number:
        if k != 0:
            if len(stack) == 0:
                stack.append(e)
            else:
                while len(stack) > 0 and k > 0:
                    if stack[-1] < e:
                        stack.pop()
                        k -= 1
                    else:
                        break
                stack.append(e)
        else:
            stack.append(e)

    answer = ''.join(stack)
    if k > 0:
        return answer[:(-1 * k)]
    else:
        return answer


print(solution('4177252841', 4))
