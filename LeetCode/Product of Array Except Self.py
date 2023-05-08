class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in range(len(nums))]
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            answer[i] *= product
        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            answer[i] *= product
        return answer