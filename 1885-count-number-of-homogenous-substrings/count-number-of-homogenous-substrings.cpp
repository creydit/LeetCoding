class Solution {
public:
    int countHomogenous(string s) {
        //Unreal magic, SEE EDITORIAL
        //TC - O(n) and sC - O(1)
        int n = s.size();
        int ans = 0;
        int curr = 0;
        for(int i = 0; i < n; i++){
            if(i==0 || s[i] == s[i-1]){
                curr++;
            }
            else curr = 1;
            ans = (ans + curr)%1000000007;
        }
        return ans;
    }
};