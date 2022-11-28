# import sys
# input = sys.stdin.readline
#
# def binary_search(target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return True
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return False
#
# n = int(input())
# array = list(map(int, input().split()))
# m = int(input())
# requests = list(map(int, input().split()))
# array.sort()
# for i in requests:
#     if binary_search(i, 0, n-1):
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
#
# # input
# # 5
# # 8 3 7 9 2
# # 3
# # 5 7 9
# #
# # output
# # no yes yes

import sys


n = int(sys.stdin.readline().rstrip())
parts = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
finds = list(map(int, sys.stdin.readline().rstrip().split()))
parts.sort()


def binary_search(arr: list, target: int) -> int:
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


for find in finds:
    idx = binary_search(parts, find)
    if idx == -1:
        print('no')
    else:
        print('yes')
