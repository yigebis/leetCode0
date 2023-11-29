class Solution {
public:
    bool isPalindrome(long x) {
        if(x<0)
        return false;
        if(x<10)
        return true;
        string s = to_string(x);
        int l = 0, r = s.length() - 1;
        while(r > l)
        {
            if (s[r] != s[l])
            return false;
            r--;
            l++;
        }
        return true;
    }
};