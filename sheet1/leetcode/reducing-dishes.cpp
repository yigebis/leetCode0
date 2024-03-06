class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        int maxVal = 0;
        int len = satisfaction.size();
        sort(satisfaction.begin(), satisfaction.end());
        int totalSum = 0;
        int initial = 0;
        for (int i = 0; i < len; i++)
        {
            totalSum += satisfaction[i];
            initial += satisfaction[i] * (i + 1);
        }
        maxVal = initial;

        int removed = 0, removedSatisfaction = 0;
        for (int i = 0; i < len; i++)
        {
            removed += satisfaction[i];
            removedSatisfaction += satisfaction[i] * (i + 1);
            int rightSum = totalSum - removed;
            int decremented = rightSum * (i + 1) + removedSatisfaction;

            maxVal = max(maxVal, initial - decremented);
        }

        return maxVal;
    }
};