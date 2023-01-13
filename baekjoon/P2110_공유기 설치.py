import sys


def get_cnt(nums, distance):
    cnt = 1
    prev = nums[0]
    for i in range(1, len(nums)):
        cur = nums[i]
        if cur - prev >= distance:
            cnt += 1
            prev= cur
    return cnt


n, c = map(int, sys.stdin.readline().rstrip().split())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))
nums = sorted(nums)

left = 0
right = nums[-1] - nums[0] + 1
max_distance = 0
while left <= right:
    mid = (left + right) // 2
    # print('left = ', left, ', right = ', right, ', mid = ', mid)
    cnt = get_cnt(nums, mid)
    if cnt < c:
        right = mid - 1
    elif cnt >= c:
        left = mid + 1
        max_distance = mid
print(max_distance)

