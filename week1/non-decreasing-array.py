class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        decreasing_count = 0
        max_left = -1 * inf
        print(max_left)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if nums[i + 1] >= max_left:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                break
            max_left = max(max_left, nums[i])
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        
        return True
        # return decreasing_count <= 1