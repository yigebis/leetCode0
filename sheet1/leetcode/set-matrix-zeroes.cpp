class Solution {
public:
    void inserter(vector<vector<int>>& matrix, unordered_set<int>rows, unordered_set<int> cols){
        for (auto row : rows){
            for (int i = 0; i < matrix[0].size(); i++){
                matrix[row][i] = 0;
            }
        }
        for (auto col : cols){
            for (int i = 0; i < matrix.size(); i++){
                matrix[i][col] = 0;
            }
        }
    }
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int>rows, cols;
        for (int i = 0; i < matrix.size(); i++){
            for (int j = 0; j < matrix[0].size(); j++){
                if (matrix[i][j] == 0){
                    rows.insert(i);
                    cols.insert(j);
                }
            }
        }
        inserter(matrix, rows, cols);
    }
};