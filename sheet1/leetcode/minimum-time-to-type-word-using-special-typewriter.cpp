class Solution {
public:
    int minTimeToType(string word) {
        int time = 0;
        char curr = 'a';
        for (int i = 0; i < word.length(); i++){
            int diff = abs(word[i] - curr);
            time += min(diff, 26 - diff);
            curr = word[i];
        }
        time += word.length();

        return time;
    }
};