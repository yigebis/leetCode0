class Solution {
public:
    bool isThere(int x, vector <int> v)
    {
        for(int i = 0; i<v.size(); i++)
        {
            if(v[i]==x)
            return true;
        }
        return false;
    }
    bool isHappy(int n) {
        if(n==1)
        return true;
        if(n==0)
        return false;
        int sum = 0;
        vector <int> v;
        v.push_back(0);
        while(true)
        {
            while(n>0)
            {
                sum+=(n%10)*(n%10);
                n/=10;
            }
            if(sum==1)
            return true;
            if(isThere(sum,v))
            return false;
            v.push_back(sum);
            n=sum;
            sum=0;
        }

    }
};