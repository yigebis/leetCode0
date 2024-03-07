class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        int minMoves = 0;
        sort(seats.begin(), seats.end());
        sort(students.begin(), students.end());
        
        for (int i = 0; i < seats.size(); i++)
        {
            minMoves += abs(seats[i] - students[i]);
        }

        return minMoves;

    }
};
// 9 15
// 0 9 
