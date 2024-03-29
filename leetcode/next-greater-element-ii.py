class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [0]
        ans = [-1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums) - 1):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        
        return ans
