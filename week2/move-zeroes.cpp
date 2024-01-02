class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, idx = 0;
        while (i < nums.size())
        {
            if (nums[i] != 0)
            {
                nums[idx] = nums[i];
                idx++;
            }
            i++;
        }
        while (idx < nums.size())
        {
            nums[idx] = 0;
            idx++;
        }

    }
};
