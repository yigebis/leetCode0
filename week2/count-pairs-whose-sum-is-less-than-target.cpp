class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        int r = nums.size() - 1;
        int l = 0, count = 0;
        sort(nums.begin(), nums.end());
        while (l < nums.size())
        {
            while (r > l)
            {
                if (nums[r] + nums[l] < target)
                {
                    count++;
                }
                r--;
            }
            r = nums.size() - 1;
            l++;
        }
        
        return count;
    }
};
//-1 1 1 2 3
//-7 -6 -2 -1 2 3 5