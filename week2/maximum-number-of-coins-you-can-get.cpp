class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int l = 0, r = piles.size() - 1;
        int counter = 0;
        sort(piles.begin(), piles.end());
        while ( l < r)
        {
            counter += piles[r-1];
            l++;
            r -= 2;   
        }
        return counter;
    }
};
// 123456789
//   ^^ 
// 1 8 9
// 2 6 7
// 3 4 5