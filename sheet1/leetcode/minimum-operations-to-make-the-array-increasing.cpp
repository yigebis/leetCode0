class Solution {
public:
    int minOperations(vector<int>& nums) {
        int operations = 0;
        int nextNum = nums[0] + 1;
        for (int i = 1; i < nums.size(); i++){
            operations += max(nextNum - nums[i], 0);
            nums[i] = max(nextNum, nums[i]);
            nextNum = nums[i] + 1;
        }

        return operations;
    }
};