class Solution {
public:
    int lengthOfLastWord(string s) {
        string word = "";
        bool seenWord = false;
        int index;
        for (int i = s.length() - 1; i >= 0; i--)
        {
            if (seenWord && s[i] == ' ')
            {
                index = i + 1;
                break;
            }
            if (s[i] != ' ')
            {
                seenWord = true;
            }
        }

        while (index < s.length() && s[index] != ' ')
        {
            word += s[index];
            index += 1;
        }
        return word.length();
    }
};