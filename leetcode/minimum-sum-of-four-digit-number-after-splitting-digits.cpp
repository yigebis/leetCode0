class Solution {
public:
    int minimumSum(int num) {
        // string s = to_string(num);
        vector<int> arr;
        for (int i = 0; i < 4; i++)
        {
            arr.push_back(num % 10);
            num /= 10;
        }
        sort(arr.begin(), arr.end());
        int num1 = arr[0] * 10 + arr[2];
        int num2 = arr[1] * 10 + arr[3];
        return num1 + num2;
    }
};