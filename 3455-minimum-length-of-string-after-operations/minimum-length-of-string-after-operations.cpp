class Solution {
public:
    int minimumLength(string s) {
        //By me FTS
        map<char,int>freq;
        for(auto i:s){
            freq[i]++;
        }
        int ans=0;
        for(auto [k,v]:freq){
            if (v>2){
                if(v%2==0){
                    ans+=2;
                }
                else{
                    ans+=1;
                }
            }
            else{
                ans+=v;
            }
        }
        return ans;
    }
};