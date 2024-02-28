class Solution {
public:
    int balancedStringSplit(string s) {
        int l = 0, r = 0, count = 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] == 'R')
            {
                r += 1;
            }
            else
            {
                l += 1;
            }
            if (l == r)
            {
                count += 1;
                l = 0;
                r = 0;
            }
        }
        return count;
    }
};