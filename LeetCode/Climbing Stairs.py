class Solution:
    def climbStairs(self, n: int) -> int:
        length = n + 1
        if n < 3:
            length = 3
        dp = [0] * length
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


print(Solution.climbStairs('', 3))