import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))
nums = sorted(nums)
# print(nums)

answer = sys.maxsize
left, right = 0, 1
while left < n - 1 and right < n:
    diff = abs(nums[right] - nums[left])
    if diff == m:
        answer = m
        break
    elif diff < m:
        right += 1
        continue
    else:
        answer = min(answer, diff)
        left += 1

print(answer)
