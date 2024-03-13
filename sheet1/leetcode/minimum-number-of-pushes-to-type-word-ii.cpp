class Solution {
public:
    int minimumPushes(string word) {
        int minPushes = 0;
        vector<int> freq(26, 0);
        for (auto ch : word){
            freq[ch - 'a']++;
        }
        sort(freq.begin(), freq.end(), greater<int>());

        for(int i = 0; i < 26; i++){
            minPushes += freq[i] * ((i/8) + 1);
        }

        return minPushes;
    }
};
// a b c d e f g h i