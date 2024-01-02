class Solution {
public:
    bool alphaNumeric (char &x)
    {
        if (x >= 48 && x<= 57)
        return true;
        if (x >= 97 && x <= 122)
        return true;
        if (x >= 65 && x <= 90)
        {
            x += 32;
            return true;
        }
        return false;
    }
    bool isPalindrome(string s) {
        int front = 0, end = s.length() - 1;
        while (front < end)
        {
            while (front < end && !alphaNumeric (s[end]))
        {
            end--;
        }   
        while (front < end && !alphaNumeric (s[front]))
        {
            front++;
        }
        if (front < end && s[end] != s[front])
        return false;
        end --;
        front++;
        }
        return true;
    }
};