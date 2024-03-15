class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        left, right = 0, len(nums) - 1
        mid = right

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1
            minimum = min(minimum, nums[mid])
        return minimum