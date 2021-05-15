# import sys
#
#
# def is_palindrome(st):
#     length = len(st)
#     if length % 2 == 0:  # 짝수
#         left = st[:length // 2]
#         right = st[length // 2:]
#         if left == right[::-1]:
#             return True
#     else:  # 홀수
#         left = st[:length // 2 + 1]
#         right = st[length // 2:]
#         if left == right[::-1]:
#             return True
#     return False
#
#
# t = int(sys.stdin.readline())
# answer = []
# for _ in range(t):
#     semi_palindrome = False
#     s = sys.stdin.readline()
#     if is_palindrome(s):
#         answer.append(0)
#         continue
#     for i in range(len(s)):
#         copy_s = list(s[:])
#         copy_s.pop(i)
#         fixed_s = ''.join(copy_s)
#         if is_palindrome(fixed_s):
#             semi_palindrome = True
#             break
#     if semi_palindrome:
#         answer.append(1)
#         continue
#     answer.append(2)
# for i in answer:
#     print(i)

import sys


def is_palindrome(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def check(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            check1 = is_palindrome(word, left + 1, right)
            check2 = is_palindrome(word, left, right - 1)
            if check1 or check2:
                return 1
            else:
                return 2
    return 0


n = int(sys.stdin.readline().rstrip("\n"))
for _ in range(n):
    word = sys.stdin.readline().rstrip("\n")
    left = 0
    right = len(word) - 1
    ans = check(word, left, right)
    print(ans)