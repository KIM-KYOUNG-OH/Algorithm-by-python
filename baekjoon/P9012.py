def is_vps(s):
    stack = [-1]
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif stack[-1]!=-1 and s[i] == ')':
            stack.pop()
        else:
            return False
    if stack[-1] != -1:
        return False
    return True

n = int(input())
for _ in range(n):
    ps = input()
    if is_vps(ps):
        print('YES')
    else:
        print('NO')