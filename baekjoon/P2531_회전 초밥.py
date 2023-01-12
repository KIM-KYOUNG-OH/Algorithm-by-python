import sys

n, d, k, c = map(int, sys.stdin.readline().rstrip().split())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))
nums.extend(nums)

answer = 0
for i in range(n):
    left = i
    right = i + k
    tmp = set(nums[left:right])
    result = len(tmp)
    if c not in tmp:
        result += 1
    answer = max(answer, result)
print(answer)
