class Solution {
public:
    int maxFreqSum(string s) {
        set<char> st = {'a','e','i','o','u'};
        unordered_map<char, int> vow;
        unordered_map<char, int> cons;
        for(auto i : s){
            if (st.find(i) != st.end()){
                vow[i]++;
            }
            else{
                cons[i]++;
            }
        }
        int mvow = 0;
        int mcon = 0;
        for (auto [x,y]  : vow){
            mvow = max(mvow, y);
        }
        for (auto [x,y]  : cons){
            mcon = max(mcon, y);
        }

        return mvow + mcon;
    }
};