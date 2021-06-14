# import sys
#
# n, jimin, hansu = map(int, sys.stdin.readline().rstrip().split())
# lst = [i for i in range(1, n + 1)]
# lst[jimin - 1] = 'j'
# lst[hansu - 1] = 'h'
# round = 0
# breaker = False  # while문 종료 조건
# while not breaker:
#     round += 1
#     temp = []
#     for i in range(1, len(lst), 2):
#         if 'j' in [lst[i], lst[i - 1]]:
#             if 'h' in [lst[i], lst[i - 1]]:
#                 breaker = True
#                 break
#             else:
#                 temp.append('j')
#             continue
#         if 'h' in [lst[i], lst[i - 1]]:
#             temp.append('h')
#             continue
#         temp.append(lst[i])
#     if len(lst) % 2 == 1:
#         temp.append(lst[-1])
#     lst = temp[:]
# print(round)

import sys

n, jimin, hansu = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
while jimin != hansu:
    jimin -= jimin // 2
    hansu -= hansu // 2
    cnt += 1
print(cnt)