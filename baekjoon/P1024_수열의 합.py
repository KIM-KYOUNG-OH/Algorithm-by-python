import sys

n, l = map(int, sys.stdin.readline().rstrip().split())
answer = ['-1']
for i in range(l, 101):
    # print('i = ', i)
    left = 0
    right = n - i + 1
    while left <= right:
        mid = (left + right) // 2
        # print('left = ', left, ', right = ', right, ', mid = ', mid)

        nums = [j for j in range(mid, mid + i)]
        total = sum(nums)
        # print('total = ', total)
        if total < n:
            left = mid + 1
        elif total == n:
            answer = list(map(str, nums))
            break
        else:
            right = mid - 1
    if answer[0] != '-1':
        break
print(' '.join(answer))
