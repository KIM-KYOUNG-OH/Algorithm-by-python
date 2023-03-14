class Solution:
    def search(self, nums, target: int) -> int:
        l = len(nums)
        left = nums.index(min(nums))
        nums.extend(nums)
        right = left + l - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                result = mid % l
                break
        return result
