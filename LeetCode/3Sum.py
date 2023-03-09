from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums) - 2):
            standard = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if standard + total == 0:
                    result.add((standard, nums[left], nums[right]))
                    left += 1
                elif standard + total < 0:
                    left += 1
                else:
                    right -= 1
        result = map(list, result)
        return result



