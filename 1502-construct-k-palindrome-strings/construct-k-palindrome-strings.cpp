class Solution {
public:
    bool canConstruct(string s, int k) {
        //POTD By me FTS (First Time Seeing)
        int n=s.size();
        if (n<k)return false;
        vector<int>v(26,0);
        for(auto i:s){
            v[i-'a']++;
        }
        int a=0;
        for(int i=0;i<26;i++){
            if(v[i]%2==1)a++;
        }
        if(a>k)return false;
        return true;
    }
};