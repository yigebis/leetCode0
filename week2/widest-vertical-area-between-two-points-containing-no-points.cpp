class Solution {
public:
    static bool customComparator(vector<int> a, vector<int> b)
    {
        return a[0] < b[0];
    }
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), customComparator);
        int widest = 0;
        for (int i = 1; i < points.size(); i++)
        {
            widest = max(widest, points[i][0] - points[i-1][0]);
        }        
        return widest;
    }
};