# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        max_right, min_right = [n - 1]*n, [n - 1]*n

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[min_right[i + 1]]:
                min_right[i] = i
            else:
                min_right[i] = min_right[i+1]

            if nums[i] > nums[max_right[i + 1]]:
                max_right[i] = i
            else:
                max_right[i] = max_right[i+1]

        # print(min_right, max_right)
        for i in range(n):
            j = i + indexDifference
            if j >= n:
                return [-1, -1]

            if abs(nums[i] - nums[min_right[j]]) >= valueDifference:
                return [i, min_right[j]]
            
            if abs(nums[i] - nums[max_right[j]]) >= valueDifference:
                return [i, max_right[j]]
        
        return [-1, -1]
            
