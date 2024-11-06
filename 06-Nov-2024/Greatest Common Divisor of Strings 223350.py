# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int len = __gcd(str1.size(), str2.size());
        string gcd = "", test = "";
        for (int i = 0; i < len; i++)
        {
            gcd += str1[i];
        }
        for (int i = 0; i < str1.size()/len; i++)
        {
            test += gcd;
        }
        if (test != str1)
        return "";
        test = "";
        for (int i = 0; i < str2.size()/len; i++)
        {
            test += gcd;
        }
        if (test != str2)
        return "";

        return gcd;

    }
};