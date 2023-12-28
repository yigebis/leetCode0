class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        // int count = 0;
        vector <int> answer(nums.size(), 0), original = nums;
        unordered_map<int,int> dict;
        // for (int i = 0; i < nums.size(); i++)
        // {
        //     for (int j = 0; j < nums.size(); j++)
        //     {
        //         if (j == i)
        //         continue;
        //         if (nums[j] < nums[i])
        //         count ++;
        //     }
        //     answer.push_back(count);
        //     count = 0;
        // }
        vector<int>counts(101, 0);
        for (auto num : nums)
        {
            counts[num] += 1;
        }
        int index = 0;
        for (int i = 0; i < counts.size(); i++)
        {
            for (int j = 0; j < counts[i]; j++)
            {
                nums[index] = i;
                index += 1;
                // dict[nums[index]] = index;
            }
        }
        for (int i = nums.size() - 1; i > - 1; i--)
        {
            dict[nums[i]] = i;
        }
        for (int i = nums.size() - 1; i > -1; i--)
        {
            answer[i] = dict[original[i]];
        }

        return answer;
    }
};