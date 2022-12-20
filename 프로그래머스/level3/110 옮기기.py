from collections import deque


def solution(ss):
    answer = []
    for s in ss:
        cnt = 0
        stack = []
        for ch in s:
            if ch == '0':
                if stack[-2:] == ['1', '1']:
                    stack.pop()
                    stack.pop()
                    cnt += 1
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        if cnt == 0:
            answer.append(s)
            continue

        result = deque()
        while stack:
            if stack[-1] == '1':
                result.appendleft(stack.pop())
            else:
                break

        while cnt != 0:
            result.appendleft('0')
            result.appendleft('1')
            result.appendleft('1')
            cnt -= 1

        while stack:
            result.appendleft(stack.pop())
        answer.append(''.join(result))
    return answer


print(solution(["1110","100111100","0111111010"]))



