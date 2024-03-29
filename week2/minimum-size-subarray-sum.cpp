class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, sum = 0, size = nums.size(), total = 0;
        for (int r = 0; r <nums.size(); r++)
        {
            sum += nums[r];
            total = sum;
            while (sum >= target)
            {
                size = min(size, r - l + 1);
                sum -= nums[l];
                l++;
            }
        }
        if (size == nums.size() && sum == total)
        return 0;
        return size;
    }
};