class Solution {
public:
    bool canConstruct(string s, int k) {
        //POTD By me FTS (First Time Seeing)
        int n=s.size();
        if (n<k)return false;
        map<char,int>mpp;
        for(auto i:s){
            mpp[i]++;
        }
        int a=0;
        for(auto i :mpp){
            if(i.second%2!=0){
                a++;
            }
        }
        if(a>k)return false;
        return true;
    }
};