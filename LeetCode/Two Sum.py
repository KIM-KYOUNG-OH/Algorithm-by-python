from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fixed_num = []
        for i, num in enumerate(nums):
            fixed_num.append((num, i))
        fixed_num.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            left_num = fixed_num[left][0]
            right_num = fixed_num[right][0]
            total = left_num + right_num
            if total == target:
                return [fixed_num[left][1], fixed_num[right][1]]
            if total < target:
                left += 1
            else:
                right -= 1


