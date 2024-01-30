class Solution {
public:
    int strStr(string haystack, string needle) {
        for (int i = 0; i < haystack.size(); i++)
        {
            if (haystack[i] == needle[0])
            {
                if (haystack.size() - i < needle.size())
                continue;
                int index = i;
                bool does_occur = true;
                for (int j = 0; j < needle.size(); j++)
                {
                    if (haystack[index] != needle[j])
                    {
                        does_occur = false;
                        break;
                    }
                    index++;
                }
                if (does_occur)
                {
                    return i;
                }
            }
        }
        return -1;
    }
};