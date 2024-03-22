class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        pos = 0
        while pos < len(nums):
            if nums[pos] == pos + 1 or nums[pos] == 0:
                pos += 1
            else:
                new_pos = nums[pos] - 1
                if nums[pos] == nums[new_pos]:
                    nums[pos] = 0
                else:
                    nums[pos], nums[new_pos] = nums[new_pos], nums[pos]
        # print(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                ans.append(i + 1)
        
        return ans
