class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0, r = s.size() - 1;
        char temp;
        while (r > l)
        {
            temp = s[r];
            s[r] = s[l];
            s[l] = temp;
            r--;
            l++;
        }
    }
};