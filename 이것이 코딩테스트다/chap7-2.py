import sys
input = sys.stdin.readline

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
array = list(map(int, input().split()))
m = int(input())
requests = list(map(int, input().split()))
array.sort()
for i in requests:
    if binary_search(i, 0, n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')

# input
# 5
# 8 3 7 9 2
# 3
# 5 7 9
#
# output
# no yes yes