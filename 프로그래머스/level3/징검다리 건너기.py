from collections import defaultdict


def solution(stones, k):
    n = len(stones)
    if n == 1:
        return stones[0]
    dp = [0] * n
    nums = sorted(set(stones), reverse=True)
    num_pos = defaultdict(list)
    for i in range(n):
        num = stones[i]
        num_pos[num].append(i)

    answer = 0
    while True:
        cur = nums.pop()
        answer += cur - answer
        for i in num_pos[cur]:
            if i == 0:
                dp[i] = dp[i + 1] + 1
                dp[i + dp[i + 1]] = dp[i]
            elif i == n - 1:
                dp[i] = dp[i - 1] + 1
                dp[i - dp[i - 1]] = dp[i]
            else:
                dp[i] = dp[i - 1] + dp[i + 1] + 1
                dp[i - dp[i - 1]] = dp[i]
                dp[i + dp[i + 1]] = dp[i]

            if dp[i] >= k:
                return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
