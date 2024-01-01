class Solution {
public:
    int temp;
    void reverser(vector<int>& arr, int start, int end)
    {
        while (start < end)
        {
            temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> ans;
        for (int i = arr.size() - 1; i > 0; i--)
        {
            for (int j = 0; j < i; j++)
            {
                if (arr[j] == i + 1)
                {
                    reverser(arr, 0, j);
                    ans.push_back(j + 1);
                    reverser(arr, 0, i);
                    ans.push_back(i + 1);
                    break;
                }
            }          
        }
       return ans;
    }
};