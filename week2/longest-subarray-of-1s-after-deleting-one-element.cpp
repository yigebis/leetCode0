class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int l = 0, len = 0, status = 1;
        for (int r = 0; r < nums.size(); r++)
        {
            if (nums[r] == 0)
            {
                status--;
            }
            if(status < 0)
            {
                if (nums[l] == 0)
                {
                    status++;
                }
                l++;
            }
            len = max(len, r - l);
        }
        
        return len;
    }
};
/*
011101101
    ^
        ^
    ^
while
    if 0 and c ! = 2
        store = r
        c += 1
    
11010101
l = 0 r = 0 c = 0
len = 0
while r + 1 < nums.size
    if nums[r] == 1
    r++
    else if && c != 1
    c++
    else
    len = max(len, r - l + 1);
    l = r
*/