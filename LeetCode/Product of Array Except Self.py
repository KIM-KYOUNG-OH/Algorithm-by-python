class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        num = 1
        for i in range(len(nums)):
            ret.append(num)
            num *= nums[i]

        num = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= num
            num *= nums[i]

        return ret