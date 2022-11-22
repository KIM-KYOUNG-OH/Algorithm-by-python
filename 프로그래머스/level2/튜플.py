from collections import Counter


def solution(s):
    lst = []
    stack = []
    tmp = ''
    for ch in list(s):
        if ch == '{':
            stack = []
            tmp = ''
        elif ch == '}':
            if tmp != '':
                stack.append(tmp)
            tmp = ''
            while stack:
                cur = stack.pop()
                lst.append(cur)
        elif ch == ',':
            stack.append(tmp)
            tmp = ''
        else:
            tmp += ch
    most_common = Counter(lst).most_common()
    answer = []
    for key, cnt in most_common:
        answer.append(int(key))
    return answer