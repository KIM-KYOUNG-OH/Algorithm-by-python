class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums[:]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], dp[i])
        return max(dp)