class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        elif n == 4:
            return max(nums[0] + nums[2], nums[1] + nums[3])
        dp_skip_first = [0] * (n - 1)
        dp_skip_first[0] = nums[1]
        dp_skip_first[1] = nums[2]
        dp_skip_first[2] = nums[3] + nums[1]
        for i in range(4, n):
            dp_skip_first[i - 1] = max(dp_skip_first[i - 3] + nums[i], dp_skip_first[i - 4] + nums[i])

        dp_skip_last = [0] * (n - 1)
        dp_skip_last[0] = nums[0]
        dp_skip_last[1] = nums[1]
        dp_skip_last[2] = nums[2] + nums[0]
        for i in range(3, n - 1):
            dp_skip_last[i] = max(dp_skip_last[i - 2] + nums[i], dp_skip_last[i - 3] + nums[i])

        return max(dp_skip_first[-1], dp_skip_first[-2], dp_skip_last[-1], dp_skip_last[-2])
