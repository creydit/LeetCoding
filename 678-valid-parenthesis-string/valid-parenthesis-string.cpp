class Solution {
public:
    bool solve(int idx, string s, int cnt, vector<vector<int>> &dp){
        if (cnt < 0 ) return false;
        if(idx == s.size()){
            return cnt == 0;
        }
        if (dp[idx][cnt] != -1) return dp[idx][cnt];
        if (s[idx] == '(') return dp[idx][cnt] = solve(idx + 1, s, cnt + 1, dp);
        if (s[idx] == ')') return dp[idx][cnt] = solve(idx + 1, s, cnt - 1, dp);
        else return dp[idx][cnt] = solve(idx + 1, s, cnt + 1, dp) || solve(idx + 1, s, cnt - 1, dp) || solve(idx + 1, s, cnt, dp);
    }
    bool checkValidString(string s) {
        //Brute Force by recursion 
        //TC - O(3^n)
        //Then optimised by using memoization
        //TC - O(n*n) and SC- O(n*n)
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n+1, -1));
        return solve(0, s, 0, dp);

    }
};