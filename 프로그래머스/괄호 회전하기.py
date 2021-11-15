from collections import deque


def is_right_bracket_string(s_list):
    stack = []
    for bracket in s_list:
        if bracket == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif bracket == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif bracket == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)
    if stack:
        return False
    return True


def solution(s):
    answer = 0
    q = deque([c for c in s])
    s_length = len(s)
    for _ in range(s_length):
        if is_right_bracket_string(q):
            answer += 1
        q.append(q.popleft())
    return answer


print(solution("}]()[{"	))