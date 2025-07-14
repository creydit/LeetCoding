class Solution {
public:
    /*
    int solve(int n, vector<int> &dp){
        if (n <= 1) return n;
        if(dp[n] != -1) return dp[n];
        return dp[n] = solve(n-1, dp) + solve(n-2, dp);
    }
    */
    int fib(int n) {
        //More Better by tabulation and DP
        //Bottom Up
        if(n==0) return 0;
        vector<int> dp(n+1, -1);
        dp[0] = 0;
        dp[1] = 1;
        for( int i = 2; i <= n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
        
        //Better by using memoization and Dp 
        //Top Down
        //TC - O(n) and SC - O(n + n) for recursion stack space and dp array
        /*
        vector<int> dp(n+1, -1);
        return solve(n, dp); 
        */

        //Brute force using plane recursion
        //TC - O(2^n) and SC - O(n) recursion stack space
        /*
        return solve(n);
        */
    }
};