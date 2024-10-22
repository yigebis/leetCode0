# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0

        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapify(nums)

        for i in range(k):
            top = -heappop(nums)
            if top == 1:
                return score + k - i
            
            score += top
            heappush(nums, -ceil(top/3))
        

        return score