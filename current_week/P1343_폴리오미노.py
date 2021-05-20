import sys

s = sys.stdin.readline().rstrip()
# s = s.replace('XXXX', 'AAAA', -1)
# s = s.replace('XX', 'BB', -1)
# if 'X' in s:
#     print(-1)
# else:
#     print(s)

s = list(s)
i = 0
while True:
    if i >= len(s):
        break
    if s[i] == 'X' and (len(s) - i) >= 4:
        if s[i + 1] == 'X' and s[i + 2] == 'X' and s[i + 3] == 'X':
            s[i], s[i + 1], s[i + 2], s[i + 3] = 'A', 'A', 'A', 'A'
            i += 4
            continue
    i += 1
i = 0
while True:
    if i >= len(s):
        break
    if s[i] == 'X' and (len(s) - i) >= 2 and s[i + 1] == 'X':
        s[i], s[i + 1] = 'B', 'B'
        i += 2
        continue
    i += 1
if 'X' in s:
    print(-1)
else:
    print(''.join(s))
