class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def score(left, right):
            if left > right:
                return 0;
            score_taking_left = nums[left] - score(left + 1, right);
            score_right = nums[right] - score(left, right - 1);
            return max(score_taking_left, score_right);
        return(score(0, len(nums) - 1) >= 0)