class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        pos = 0
        duplicates = []
        while pos < len(nums):
            if nums[pos] == 0:
                pos += 1
            elif nums[pos] != pos + 1:
                new_pos = nums[pos] - 1
                if nums[pos] == nums[new_pos]:
                    nums[pos] = 0
                    duplicates.append(nums[new_pos])
                else:
                    nums[new_pos], nums[pos] = nums[pos], nums[new_pos]
            else:
                pos += 1
            # print(nums, duplicates)
        return duplicates

# 7,3,2,4,8,2,3,1