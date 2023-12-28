class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        unordered_map<int, string> hasher;
        vector<string> ans;
        for (int i = 0; i < heights.size(); i++)
        {
            hasher[heights[i]] = names[i];
        }
        sort(heights.begin(), heights.end());
        reverse(heights.begin(), heights.end());
        for (int i : heights)
        {
            ans.push_back(hasher[i]);
        }
        return ans;
    }
};