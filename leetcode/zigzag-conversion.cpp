class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1)
        {
            return s;
        }
        vector<vector<int>> rows(numRows);
        string afterZigzag = "";
        int row = 0, len = s.size();
        char phase = '+';


        for (int i = 0; i < len; i++)
        {
            if (phase == '+' && row == numRows)
            {
                row -= 2;
                phase = '-';
            }
            else if (phase == '-' && row == -1)
            {
                row += 2;
                phase = '+';
            }
            rows[row].push_back(s[i]);
            if (phase == '+')
            {
                row += 1;
            }
            else
            {
                row -= 1;
            }
        }
        
        for (int i = 0; i < rows.size(); i++)
        {
            for (int j = 0; j < rows[i].size(); j++)
            {
                afterZigzag += rows[i][j];
            }
        }
        return afterZigzag;
    }
};
// PAYPALISHIRING 3
// 01210121012101
// 0 4 8 12...
// 1 3 5 7 9 ... 
// 2 6 10 ...
// PAYPALISHIRING 4
// 01232101232101
// 0 6 12 ...
// 1 5 9 13...
// 2 
// PAYPALISHIRING 5
// 01234321012343
// 0 8 16