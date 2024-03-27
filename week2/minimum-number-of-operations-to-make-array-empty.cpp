class Solution {
public:
    int minOperations(vector<int>& nums) {
        int minOperation = 0, count; 
        unordered_map<int, int> freq;
        for (auto num : nums){
            freq[num]++;
        }

        for (auto it : freq){
            count = it.second;
            if (count == 1){
                return -1;
            }
            minOperation += count/3;
            if (count % 3 != 0){
                minOperation++;
            }
        }

        return minOperation;
    }
};