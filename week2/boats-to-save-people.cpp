class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int r = people.size() - 1, l = 0, count = 0;
        while (r >= l)
        {
            if (r == l)
            {
                count++;
                r--;
                l++;
            }
            else if (people[r] == limit)
            {
                r--;
                count++;

            }
            else if (people[r] + people[l] <= limit)
            {
                r--;
                l++;
                count++;
            }
            else{
                count++;
                r--;
            }
        }
        return count;
    }
};
// 1 1 2 3 4 4 5 6 7 7 8  limit = 9
//