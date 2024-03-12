class Solution {
    unordered_set<string> appearance;
    string ans = "";
public:
    void backtrack(string s, int size){
        if (s.length() == size){
            if (appearance.find(s) == appearance.end()){
                ans = s;
            }
            return;
        }
        
        for (int i = 0; i <= 1; i++){
            if (ans.size() != 0){
                return;
            }
            s += ('0' + i);
            backtrack(s, size);
            s.pop_back();
        }
    }
    string findDifferentBinaryString(vector<string>& nums) {
        for (auto num : nums){
            appearance.insert(num);
        }

        backtrack("", nums.size());
        return ans;
    }
};