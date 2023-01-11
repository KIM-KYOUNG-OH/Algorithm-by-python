import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))

nums = sorted(nums)
answer = 0
for i in range(n):
    tmp = nums[:i] + nums[i + 1:]
    left, right = 0, len(tmp) - 1
    while left < right:
        t = tmp[left] + tmp[right]
        if t == nums[i]:
            answer += 1
            break
        if t < nums[i]:
            left += 1
        else:
            right -= 1
print(answer)
