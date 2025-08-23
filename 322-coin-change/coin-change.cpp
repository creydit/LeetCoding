class Solution {
public:
    int solve(int idx, vector<int> &arr, int T, vector<vector<int>> &dp){
        if(idx == 0){
            if ( T % arr[idx] == 0) return T/arr[idx];
            return 1e9;
        }
        if(dp[idx][T] != -1) return dp[idx][T];

        int  nottake = solve(idx - 1, arr, T, dp);
        int take = 1e9;
        if (arr[idx] <= T) take = 1 + solve(idx, arr, T - arr[idx], dp);

        return dp[idx][T] = min(take, nottake);
    }
    int coinChange(vector<int>& coins, int amount) {
        //By Recursion + DP + Memoization //Top Down
        //TC - O(n*amt) and SC - O(n*amt + n)
        int n = coins.size();
        vector<vector<int>> dp(n, vector<int> (amount+1, -1));
        int ans = solve(n - 1, coins, amount, dp);
        if (ans >= 1e9) return -1;
        return ans;
    }
};