class RandomizedSet {
public:
    vector<int>values;
    unordered_map<int, int>index;
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (index.find(val) == index.end())
        {
            values.push_back(val);
            index[val] = values.size() - 1;
            return true;
        }
        else
        {
            return false;
        }
    }
    
    bool remove(int val) {
        if (index.find(val) == index.end())
        {
            return false;
        }
        
        index.erase(val);
        return true;
    }
    
    int getRandom() {
        int random = rand() % index.size();
        auto it = index.begin();
        for (int i = 0; i < random; i++)
            it++;
        return it -> first;
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */