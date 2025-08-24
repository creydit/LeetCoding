class Solution {
public:
    int solve(int idx, vector<int> &coins, int target, vector<vector<int>> &dp){
        if(idx == 0){
            if( target % coins[0] == 0) return 1;
            else return 0;
        }
        if(dp[idx][target] != -1) return dp[idx][target];

        int nottake = 0 + solve(idx - 1, coins, target, dp);
        int take = 0;
        if (coins[idx] <= target) take = solve(idx, coins, target - coins[idx], dp);

        return dp[idx][target] = take + nottake;
    }
    int change(int amount, vector<int>& coins) {
        //By coin change logic instead if just calculating money we just count it in 1 way to apporach answer
        //By Recursion + DP + memoization
        //TC - O(n*amount) and SC - O(n*amount + 1)
        int n = coins.size();
        vector<vector<int>> dp(n, vector<int>(amount+1, -1));
        return solve(n-1, coins, amount, dp);
    }
};