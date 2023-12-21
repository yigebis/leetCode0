class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        pre_zero, post_one = [0 for i in range(len(nums) + 1)], [0 for i in range(len(nums) + 1)]
        high_score = 0
        high_scores = []
        for i in range(len(nums)):
            if nums[i] == 0:
                pre_zero[i + 1] = 1 + pre_zero[i]
            else:
                pre_zero[i + 1] = pre_zero[i]
        j = len(nums) - 1
        while j > -1:
            if nums[j] == 1:
                post_one[j] = 1 + post_one[j+1]
            else:
                post_one[j] = post_one[j+1]
            j -= 1
        
        for i in range(len(nums)  + 1):
            high_score = max(high_score, pre_zero[i] + post_one[i])
        
        for i in range(len(nums) + 1):
            if pre_zero[i] + post_one[i] == high_score:
                high_scores.append(i)
                
        return high_scores
            
