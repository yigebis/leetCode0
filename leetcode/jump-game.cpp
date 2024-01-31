class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_index = 0;
        for (int i = 0; i < nums.size() - 1; i++)
        {
            if (nums[i] == 0 && i >= max_index)
            {
                return false;
            }
            max_index = max(max_index, i + nums[i]);
        }
        return true;
    }
};
// 4 2 0 2 1 0 3 3 0 11 2 0 2
// 