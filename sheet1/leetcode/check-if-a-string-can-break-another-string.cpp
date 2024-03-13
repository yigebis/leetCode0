class Solution {
public:
    bool checkIfCanBreak(string s1, string s2) {
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());

        int c1 = 0, c2 = 0;

        for (int i = 0; i < s1.length(); i++){
            if (s1[i] >= s2[i]){
                c1++;
            }
            if (s2[i] >= s1[i]){
                c2++;
            }
        }
        if (c1 == s1.length() || c2 == s2.length()){
            return true;
        }
        return false;
    }
};
// cdeeeelot
// eeiinrtvw