class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;
        vector<int> ans;
        while (r > l)
        {
            if (numbers[l] + numbers[r] == target)
            {
                ans.push_back(l + 1);
                ans.push_back(r + 1);
                break;
            }
            else if (numbers[l] + numbers[r] > target)
            {
                r--;
            }
            else
            {
                l++;
            }
        }
        return ans;
    }
};

// 2 6 7 9 11 15  15, 16, 11