class Solution {
public:
    void swap(int& x, int &y)
    {
        int temp = x;
        x = y;
        y = temp;
    }
    void sortColors(vector<int>& nums) {
        int ptr1 = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == 0)
            {
                swap(nums[i],nums[ptr1]);
                ptr1++;
            }
        }
        for (int i = ptr1; i < nums.size(); i++)
        {
            if (nums[i] == 1)
            {
                swap(nums[i],nums[ptr1]);
                ptr1++;
            }   
        }
    }
};