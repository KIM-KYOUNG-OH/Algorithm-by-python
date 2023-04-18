import sys


class Solution:
    def maxProduct(self, nums) -> int:
        answer = nums[0]
        product = 1
        for i in range(len(nums) - 1):
            product *= nums[i]
            answer = max(answer, product)
            if product == 0:
                product = 1

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            answer = max(answer, product)
            if product == 0:
                product = 1

        return answer