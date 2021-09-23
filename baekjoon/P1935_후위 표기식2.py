import sys

n = int(sys.stdin.readline().rstrip())
expression = sys.stdin.readline().rstrip()
alp_dic = dict()
for i in range(65, n + 65):
    alp_dic[chr(i)] = int(sys.stdin.readline().rstrip())
stack = []

for ch in expression:
    if ch.isupper():  # 대문자 알파벳이면
        stack.append(alp_dic[ch])
    else:  # 연산자이면
        value2 = stack.pop()
        value1 = stack.pop()
        if ch == '+':
            stack.append(value1 + value2)
        elif ch == '-':
            stack.append(value1 - value2)
        elif ch == '*':
            stack.append(value1 * value2)
        elif ch == '/':
            stack.append(value1 / value2)

print('{:.2f}'.format(stack.pop()))