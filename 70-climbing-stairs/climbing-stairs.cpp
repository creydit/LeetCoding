class Solution {
public:
    int solve(int n, vector<int> &dp){
        if(n <= 1) return 1;
        if(dp[n] != -1) return dp[n];
        int l = solve(n-1, dp);         //1 step climb
        int r = solve(n-2, dp);         //2 step climb
        return dp[n] = l + r;
    }
    int climbStairs(int n) {
        //Better by memoization and DP
        //top down
        //TC - O(n) and SC - O(n+n)
        vector<int> dp(n+1, -1);
        return solve(n, dp);

        //Brute force plain recursion 
        //TC - O(2^n) and SC - O(n) recursion stack space
        /*
        return solve(n);
        */
    }
};