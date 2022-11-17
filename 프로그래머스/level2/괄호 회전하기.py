from collections import deque


def is_correct(q):
    stack = deque([])
    for ch in q:
        if ch == '[' or ch == '(' or ch == '{':
            stack.append(ch)
        elif not stack:
            return False
        elif ch == ']':
            if stack[-1] != '[':
                return False
            else:
                stack.pop()
        elif ch == ')':
            if stack[-1] != '(':
                return False
            else:
                stack.pop()
        elif ch == '}':
            if stack[-1] != '{':
                return False
            else:
                stack.pop()

    if stack:
        return False
    return True


def solution(s):
    n = len(s)
    q = deque(list(s))
    answer = 0
    for _ in range(n):
        q.append(q.popleft())
        if is_correct(q):
            answer += 1

    print(answer)
    return answer


solution("[](){}")