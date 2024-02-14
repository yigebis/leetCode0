class Solution {
public:
    bool isValid(int a, int b, int c)
    {
        return a + b > c  && a + c > b && b + c > a;
    }
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = nums.size() - 1; i >= 2; i--)
        {
            if (isValid(nums[i], nums[i-1], nums[i-2]))
            {
                return nums[i] + nums[i-1] + nums[i-2];
            }
        }
        return 0;
    }
};
// 10 2 1 1
