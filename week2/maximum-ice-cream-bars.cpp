class Solution {
public:
    vector<int> maximini(vector<int>arr)
    {
        int maxi = 0, mini = 1000000;
        for (auto i : arr)
        {
            maxi = max(maxi, i);
            mini = min(mini, i);
        }
        return {maxi, mini};
    }
    int maxIceCream(vector<int>& costs, int coins) {
        int index = 0;
        int count = 0;
        vector<int> maxmin = maximini(costs);
        int maxVal = maxmin[0];
        int minVal = maxmin[1];
        vector<int>cSort(maxVal - minVal + 1, 0);
        
        for (auto cost : costs)
        {
            cSort[cost - minVal] += 1;
        }

        for (int i = 0; i < cSort.size(); i++)
        {
            for (int j = 0; j < cSort[i]; j++)
            {
                costs[index] = i + minVal;
                index += 1;
            }
        }

        for (int i = 0; i < costs.size(); i++)
        {
            if (coins < costs[i])
            break;
            count++;
            coins -= costs[i];
        }
        return count;
    }
};