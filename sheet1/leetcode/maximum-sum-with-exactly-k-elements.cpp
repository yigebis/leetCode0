class Solution {
public:
    int maximum(vector<int> nums){
        int maxVal = nums[0];
        for (int i = 1; i < nums.size(); i++){
            maxVal = max(maxVal, nums[i]);
        }
        return maxVal;
    }
    int maximizeSum(vector<int>& nums, int k) {
        int score = 0;
        // finding the maximum value
        int maxVal = maximum(nums);
        score = maxVal;
        
        for (int i = 0; i < k - 1; i++){
            maxVal++;
            score += maxVal;
        }

        return score;
    }
};