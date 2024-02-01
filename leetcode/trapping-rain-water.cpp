class Solution {
public:
    int trap(vector<int>& height) {
        // O(n) time and O(n) memory
        vector<int> maxLeft(height.size(), 0), maxRight(height.size(), 0);
        int trapped = 0;
        
        for (int i = 1; i < height.size(); i++)
        {
            maxLeft[i] = max(height[i-1], maxLeft[i-1]);
        }
        for (int i = height.size() - 2; i >= 0; i--)
        {
            maxRight[i] = max(height[i+1], maxRight[i+1]);
        }

        for (int i = 0; i < height.size(); i++)
        {
            trapped += max(0, min(maxRight[i], maxLeft[i]) - height[i]);
        }

        return trapped;
    }
};