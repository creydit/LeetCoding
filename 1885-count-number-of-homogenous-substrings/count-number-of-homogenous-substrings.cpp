class Solution {
public:
    int countHomogenous(string s) {
        //Unreal magic, SEE EDITORIAL
        //TC - O(n) and sC - O(1)
        int n = s.size();
        int ans = 1;
        int curr = 1;
        int m = 1000000007;
        for(int i = 1; i < n; i++){
            if(s[i] == s[i-1])curr++;
            else curr = 1;
            ans = (ans + (curr%m) ) % m;
        }
        return ans;
    }
};