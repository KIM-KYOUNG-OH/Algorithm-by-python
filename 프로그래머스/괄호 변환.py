def divide_u_v(s):
    u, v = '', ''
    bracket_cnt = {'(': 0, ')': 0}
    for i, bracket in enumerate(s):
        if bracket == '(':
            bracket_cnt['('] += 1
        else:
            bracket_cnt[')'] += 1
        if bracket_cnt['('] == bracket_cnt[')']:
            u = s[:i + 1]
            v = s[i + 1:]
            break
    return u, v


def is_right_bracket_string(s):
    stack = []
    for b in s:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if not stack:
        return True
    else:
        return False


def solution(w):
    if w == '':
        return ''
    u, v = divide_u_v(w)

    if is_right_bracket_string(u):
        return u + solution(v)
    else:  # u가 올바른 괄호 문자열이 아닌 경우
        answer = '(' + solution(v) + ')'
        for b in u[1:-1]:
            if b == '(':
                answer += ')'
            else:
                answer += '('
        return answer


print(solution("()))((()"))