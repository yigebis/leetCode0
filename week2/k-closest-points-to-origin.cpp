class Solution {
public:
    static bool customComparator(vector<int> a, vector<int>b)
    {
        int disA = abs(a[0]) * abs(a[0]) + abs(a[1]) * abs(a[1]);
        int disB = abs(b[0]) * abs(b[0]) + abs(b[1]) * abs(b[1]);
        return disA < disB;
    }
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        sort(points.begin(), points.end(), customComparator);
        vector<vector<int>> kClosest;
        for (int i = 0; i < k; i++)
        {
            kClosest.push_back(points[i]);
        }
        return kClosest;
    }
};