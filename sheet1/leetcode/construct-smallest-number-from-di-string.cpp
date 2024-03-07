class Solution {
public:
    void print(vector<int> arr)
    {
        for (auto i : arr)
        {
            cout<<i<<" ";
        }
    }
    string smallestNumber(string pattern) {
        string smallest = "";
        vector<int> nextI(pattern.length(), pattern.length());

        for (int i = pattern.length() - 2; i >= 0; i--)
        {
            if (pattern[i+1] == 'I'){
                nextI[i] = i + 1;
            }
            else{
                nextI[i] = nextI[i+1];
            }          
        }
        // print(nextI);
        int maxNum = 0;
        if (pattern[0] == 'I')
            maxNum = 1;
        else
            maxNum = nextI[0] + 1;
        int prevNum = maxNum;
        smallest += to_string(prevNum);

        for (int i = 0; i < pattern.length(); i++){
            if (pattern[i] == 'I'){
                smallest += to_string(maxNum + nextI[i] - i);
                maxNum = max(maxNum, maxNum + nextI[i] - i);
                // cout<<endl<<maxNum;
            }
            else{
                smallest += to_string(prevNum - 1);
            }
            prevNum = smallest[i+1] - '0';
        }

        return smallest;
    }
};
// IIIDIDDD
// 123