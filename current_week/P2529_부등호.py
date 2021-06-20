# import sys
# from itertools import permutations
#
# k = int(sys.stdin.readline().rstrip())
# brackets = sys.stdin.readline().rstrip().split()
# numbers = [i for i in range(10)]
# candidates = list(permutations(numbers, k + 1))
# answer = []
# for candidate in candidates:
#     breaker = False
#     for i in range(k):
#         if brackets[i] == '<':
#             if candidate[i] > candidate[i + 1]:
#                 breaker = True
#                 break
#         elif brackets[i] == '>':
#             if candidate[i] < candidate[i + 1]:
#                 breaker = True
#                 break
#     if breaker:
#         continue
#     answer.append(''.join(map(str, candidate)))
# answer.sort()
# print(answer[-1])
# print(answer[0])
import sys


def is_possible(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True


def recursive(cnt, num):
    global min_num, max_num
    if cnt > n:
        if not len(min_num):
            min_num = num
        else:
            max_num = num
        return
    for i in range(10):
        if not check[i]:
            if cnt == 0 or is_possible(num[-1], str(i), brackets[cnt - 1]):
                check[i] = True
                recursive(cnt + 1, num + str(i))
                check[i] = False


n = int(sys.stdin.readline().rstrip())
brackets = sys.stdin.readline().rstrip().split()
check = [False] * 10
max_num, min_num = '', ''
recursive(0, '')
print(max_num)
print(min_num)