class Solution {
public:
    unordered_set<int> pos_seen, neg_seen;
    bool checkForward(int i, vector<int>& nums)
    {
        int lastIndex = i;
        unordered_set<int> path;

        while (true)
        {
            if (nums[i] < 0)
            {
                break;
            }
            if (path.find(i) != path.end())
            {
                if (lastIndex != i)
                {
                    return true;
                }
                else
                {
                    return false;
                }   
            }
            if (pos_seen.find(i) != pos_seen.end())
            {
                return false;
            }
            
            pos_seen.insert(i);
            path.insert(i);
            lastIndex = i;
            i = i + nums[i];
            i %= nums.size();
        }
        return false;
    }
    bool checkBackward(int i, vector<int> nums)
    {
        int lastIndex = i;
        unordered_set<int> path;
        while (true)
        {
            if (nums[i] > 0)
            {
                return false;
            }
            if (path.find(i) != path.end())
            {
                if (lastIndex != i)
                {
                    return true;
                }
            }
            if (neg_seen.find(i) != neg_seen.end())
            {
                cout<<"wow";
                return false;
            }
            path.insert(i);
            neg_seen.insert(i);
            lastIndex = i;
            i = i + nums[i];
            int size = nums.size();
            i = i % (size);
            if (i < 0)
            {
                i = nums.size() + i;
            }
        }
        return false;
    }
    bool circularArrayLoop(vector<int>& nums) {
        // positive pass
        for (int i = 0; i < nums.size(); i++)
        {
            if (checkForward(i, nums))
            {
                return true;
            }
            if (checkBackward(i, nums))
            {
                return true;
            }
        }
        cout<<"  "<<(-1) % 5;
        return false;

        // negative pass
    }
};