import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
left, right = 0, 1
cnt = 0
while left <= right <= n:
    sum_nums = nums[left:right]
    total = sum(sum_nums)

    if total == m:
        cnt += 1
        right += 1
    elif total < m:
        right += 1
    else:
        left += 1
print(cnt)

# answer = 0
# for i in range(n):
#     total = 0
#     for j in range(i, n):
#         total += nums[j]
#         if total == m:
#             answer += 1
#             break
#         elif total > m:
#             break
# print(answer)
