class Solution {
public:
    int minPartitions(string n) {
        char max_num = n[0];
        for (int i = 1; i < n.length(); i++)
        {
            max_num = max(max_num, n[i]);
        }
        // cout<<max_num;
        return max_num - '0';
    }
};