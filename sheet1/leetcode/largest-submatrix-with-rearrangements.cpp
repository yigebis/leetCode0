class Solution {
public:
    void print(vector<int> arr, unordered_map<int, int> freq){
        for (int i = 0; i < arr.size(); i++){
            cout<<arr[i]<<","<<freq[arr[i]]<<" ";
        }
        cout<<endl;
    }
    int largestSubmatrix(vector<vector<int>>& matrix) {
        unordered_map<int, int> colCount;
        int maxArea = 0;
        for (int i = 0; i < matrix.size(); i++)
        {
            // int minCount = 100000, maxCount = 0;
            unordered_map<int, int> freq;
            for (int j = 0; j < matrix[0].size(); j++){
                if (matrix[i][j] == 0 && colCount.find(j) != colCount.end()){
                    colCount.erase(j);
                }
                else if (matrix[i][j] == 1){
                    colCount[j] += 1;
                    freq[colCount[j]] += 1;
                    // maxCount = max(maxCount, colCount[j]);
                    // minCount = min(minCount, colCount[j]);
                }
            }
            // cout<<minCount<<" "<<maxCount<<" "<<colCount.size()<<endl;
            vector<int> arr;
            int nextSize = colCount.size();
            int maxInRow = 0;
            for (auto it : freq){
                arr.push_back(it.first);
            }
            sort(arr.begin(), arr.end());
            // print(arr, freq);
            for (int k = 0; k < arr.size(); k++){
                maxInRow = max(maxInRow, arr[k] * nextSize);
                nextSize -= freq[arr[k]];
            }
            
            maxArea = max(maxArea, maxInRow);
        }
        
        return maxArea;
    }
};
/*
1 0 1
1 0 1
0 1 1
0 1 0
0 0 0
0 1 1
*/