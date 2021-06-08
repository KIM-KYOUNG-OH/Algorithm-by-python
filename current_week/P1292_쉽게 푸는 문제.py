# import sys
#
# a, b = map(int, sys.stdin.readline().rstrip().split())
# dp = [0] * 46
# for i in range(1, 46):
#     dp[i] = dp[i - 1] + i
# num = 0
# for i in range(1, 46):
#     num = i
#     if dp[i] > b:
#         break
# lst = [0]
# for i in range(1, num + 1):
#     for _ in range(i):
#         lst.append(i)
# print(sum(lst[a:b + 1]))

number_list = []
for i in range(1, 46):
    number_list += [i] * i

A, B = map(int, input().split())
print(sum(number_list[A - 1:B]))