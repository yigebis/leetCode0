class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = prices[0];
        int max_profit = 0;
        for (int i = 1; i < prices.size(); i++)
        {
            if (prices[i] < prices[i-1])
            {
                max_profit += prices[i-1] - min_price;
                min_price = prices[i];
            }
        }
        max_profit += prices[prices.size() - 1] - min_price;
        return max_profit;
    }
};
// 1 8 2 10 4 4 5 8 9
// 1 5 7
// 5 + 5= 10
// a, b, c, d
// b-a + d-c   d - a
// d - a + b - c    d - a