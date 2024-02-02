class Solution {
public:
    string intToRoman(int num) {
        // unordered_map<int, char> toRoman = {
        //     {1 , 'I'},
        //     {5 , 'V'},
        //     {10 , 'X'},
        //     {50 , 'L'},
        //     {100 , 'C'},
        //     {500 , 'D'},
        //     {1000 , 'M'}
        // };
        string intToRoman = "";
        int val = num;

        while (val > 0)
        {
            if (val >= 1000)
            {
                intToRoman += 'M';
                val -= 1000;
            }
            else if (val >= 900)
            {
                intToRoman += "CM";
                val -= 900;
            }
            else if (val >= 500)
            {
                intToRoman += 'D';
                val -= 500;
            }
            else if (val >= 400)
            {
                intToRoman += "CD";
                val -= 400;
            }
            else if (val >= 100)
            {
                intToRoman += 'C';
                val -= 100;
            }
            else if (val >= 90)
            {
                intToRoman += "XC";
                val -= 90;
            }
            else if (val >= 50)
            {
                intToRoman += 'L';
                val -= 50;
            }
            else if (val >= 40)
            {
                intToRoman += "XL";
                val -= 40;
            }
            else if (val >= 10)
            {
                intToRoman += 'X';
                val -= 10;
            }
            else if (val >= 9)
            {
                intToRoman += "IX";
                val -= 9;
            }
            else if (val >= 5)
            {
                intToRoman += 'V';
                val -= 5;
            }
            else if (val >= 4)
            {
                intToRoman += "IV";
                val -= 4;
            }
            else
            {
                intToRoman += 'I';
                val -= 1;
            }
        }
        return intToRoman;
    }
};
// 1 -> 0
// 5 -> 1
// 10 -> 2
// 50 -> 10
// 100 -> 20
// 500 -> 100
// 1000 -> 200