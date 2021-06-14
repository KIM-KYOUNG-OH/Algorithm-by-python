# import sys
#
# A, B = sys.stdin.readline().rstrip().split()
# length_diff = len(B) - len(A)
# answer = int(1e9)
# for left_length in range(length_diff + 1):
#     right_length = length_diff - left_length
#     fixed_A = B[:left_length] + A + B[len(B) - right_length:]
#     cnt = 0
#     for i in range(len(fixed_A)):
#         if fixed_A[i] != B[i]:
#             cnt += 1
#     answer = min(answer, cnt)
# print(answer)

import sys

A, B = sys.stdin.readline().rstrip().split()
answer = 50
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            cnt += 1
    answer = min(answer, cnt)
print(answer)