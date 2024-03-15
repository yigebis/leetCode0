class Solution {
public:
    int maxJump(vector<int>& stones) {
        if (stones.size() == 1){
            return 0;
        }
        int minCost = stones[1] - stones[0];
        for (int i = 3; i < stones.size(); i += 2){
            int currCost = stones[i] - stones[i-2];
            minCost = max(minCost, currCost);
        }
        for (int i = 2; i < stones.size(); i += 2){
            int currCost = stones[i] - stones[i-2];
            minCost = max(minCost, currCost);
        }

        return minCost;
    }
};