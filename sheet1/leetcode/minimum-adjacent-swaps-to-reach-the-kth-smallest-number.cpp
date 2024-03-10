class Solution {
public:
    // int nextPermutation(string num){
    //     int j = num.length() - 1;
    //     while
    // }
    // 11112
    // 21111
    int minSteps(string num1, string num2){
        int swaps = 0;
        int holder = 0;
        while (holder < num2.length())
        {
            int seeker = holder;
            while (num1[seeker] != num2[holder]){
                seeker++;
            }
            while (holder < seeker)
            {
                int temp = num1[seeker - 1];
                num1[seeker - 1] = num1[seeker];
                num1[seeker] = temp;
                swaps++;
                seeker--;
            }
            holder++;
        }
        return swaps;
    }
    int getMinSwaps(string num, int k) {
        string original = num;
        for (int i = 0; i < k; i++)
        {
            next_permutation(num.begin(), num.end());
        }
        return minSteps(original, num);
    }
};