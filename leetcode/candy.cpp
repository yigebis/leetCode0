class Solution {
public:
    int candy(vector<int>& ratings) {
        int len = ratings.size();
        int totalMins = 0;
        vector<int> minCandies(len, 1);

        for (int i = 1; i < len; i++)
        {
            if (ratings[i] > ratings[i-1])
            {
                minCandies[i] = minCandies[i-1] + 1;
            }
        }
        for (int i = len - 2; i >= 0; i--)
        {
            if (ratings[i] > ratings[i+1])
            {
                minCandies[i] = max(minCandies[i],minCandies[i+1] + 1);
            }
        }

        for (int i = 0; i < len; i++)
        {
            totalMins += minCandies[i];
        }
        return totalMins;
    }
};
// 1,0,2,3,10,6,4,12,8,9
// 


