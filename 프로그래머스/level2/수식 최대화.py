from itertools import permutations
from collections import deque


def operation(left, right, op):
    if op == '*':
        return left * right
    elif op == '+':
        return left + right
    else:
        return left - right


def calculate(expression, candidate):
    q = deque([])
    tmp = ''
    for ch in list(expression):
        if ch.isdigit():
            tmp += ch
        else:
            q.append(tmp)
            q.append(ch)
            tmp = ''
    if len(tmp):
        q.append(tmp)

    for op in candidate:
        stack = deque([])
        while len(q) != 0:
            cur = q.popleft()
            if cur == op:
                stack.append(operation(int(stack.pop()), int(q.popleft()), op))
            else:
                stack.append(cur)
        q = stack

    return abs(int(q[0]))


def solution(expression):
    answer = []
    op = ['*', '+', '-']
    candidates = permutations(op, 3)
    for candidate in candidates:
        answer.append(calculate(expression, candidate))
    return max(answer)


solution("100-200*300-500+20")