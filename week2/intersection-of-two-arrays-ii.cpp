class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int>freq1, freq2;
        vector<int>ans;
        for (auto num : nums1)
        {
            freq1[num]++;
        }
        for (auto num : nums2)
        {
            freq2[num]++;
        }
        for (auto f : freq1)
        {
            freq1[f.first] = min(freq1[f.first], freq2[f.first]);
            for (int i = 0; i < freq1[f.first]; i++)
                ans.push_back(f.first);
        }
        return ans;
    }
};