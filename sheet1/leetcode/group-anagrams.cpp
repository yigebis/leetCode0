class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> anagrams;
        unordered_map<string, vector<string>> group;

        for (int i = 0; i < strs.size(); i++)
        {
            string original = strs[i];
            sort(strs[i].begin(), strs[i].end());
            group[strs[i]].push_back(original);
        }

        for (auto it : group)
        {
            anagrams.push_back(it.second);
        }

        return anagrams;
    }
};