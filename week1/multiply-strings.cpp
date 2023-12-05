class Solution {
public:
    int toInt(char x)
    {
        return x - '0';
    }
    string multiply(string num1, string num2) {
        // for (int i = 0; i < num1.length(); i++)
        // {
        //     for (int j = 0; j < num2.length(); j++)
        //     {
        //         (num1[i] - "0") * (num2[j] - "0")
        //     }
        // }
        if (num1[0] == '0')
        return num1;
        if (num2[0] == '0')
        return num2;
        vector <int> result ((num1.length() + num2.length()), 0);

        for(int i = num1.length() - 1; i >= 0; i--)
        {
            for (int j = num2.length() - 1; j >= 0; j--)
            {
                result[i + j + 1] += (toInt(num1[i]) * toInt(num2[j]));
                result[i + j] += result[i + j + 1] / 10;
                result[i + j + 1] %= 10;  
            } 
        }
        string final = "";
        int i = 0;
        while (result[i] == 0)
        i++;
        while (i < result.size())
        {
            final += to_string(result[i]);
            i++;
        }
        return final;        
    }
};