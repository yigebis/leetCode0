class Solution {
public:
    int hIndex(vector<int>& citations) {
        // int hIndex = 0;
        int size = citations.size();

        sort(citations.begin(), citations.end());
        for (int i = 0; i < size; i++)
        {
            if (size - i <= citations[i])
            {
                return size - i;
            }
        }
        return 0;
    }
};
// 0 1 3 5 6
// 1 1 3
// 2 3 5 50 100