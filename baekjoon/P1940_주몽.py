import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums = sorted(nums)
left = 0
right = len(nums) - 1
answer = 0
while left < right:
    total = nums[left] + nums[right]
    if total > m:
        right -= 1
    elif total == m:
        answer += 1
        left += 1
    else:
        left += 1
print(answer)