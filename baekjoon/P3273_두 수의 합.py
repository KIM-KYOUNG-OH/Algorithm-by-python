import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())

nums = sorted(nums)
answer = 0
left, right = 0, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
    if total > x:
        right -= 1
    elif total == x:
        answer += 1
        left += 1
    else:
        left += 1
print(answer)
