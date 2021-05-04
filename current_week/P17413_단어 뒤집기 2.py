def print_stack():
    global ans
    while stack:
        ans += stack.pop()


s = input()
stack = []
is_tag = False
ans = ''
for ch in s:
    if ch == '<':  # '<'가 나오면 스택을 비움
        print_stack()
        is_tag = True
        ans += ch
        continue
    if ch == ' ':   # 공백이 나오면 스택을 비움
        print_stack()
        ans += ch
        continue
    if ch == '>':
        ans += ch
        is_tag = False
        continue
    if is_tag:  # 태그안의 문자
        ans += ch
        continue
    stack.append(ch)
print_stack()
print(ans)