class Solution {
public:
    /*
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
    */
    int coinChange(vector<int>& coins, int amount) {
        //Space Optimised 
        //TC - O(n*amt) and SC - O(amt)
        int n = coins.size();
        vector<int> prev(amount+1, 0), curr(amount+1, 0);
        for(int T = 0; T <= amount; T++){
            if (T % coins[0] == 0) prev[T] = T / coins[0];
            else prev[T] = 1e9;
        }
        for(int i = 1; i < n; i++){
            for(int T = 0; T <= amount; T++){
                int  nottake = prev[T];
                int take = 1e9;
                if (coins[i] <= T) take = 1 + curr[T - coins[i]];
                curr[T] = min(take, nottake);
            }
            prev = curr;
        }
        int ans = prev[amount];
        if (ans >= 1e9) return -1;
        return ans;
        //By Tabulation 
        //TC - O(n*amt) and SC - O(n*amt)
        /*
        int n = coins.size();
        vector<vector<int>> dp(n, vector<int> (amount+1, 0));
        for(int T = 0; T <= amount; T++){
            if (T % coins[0] == 0) dp[0][T] = T / coins[0];
            else dp[0][T] = 1e9;
        }
        for(int i = 1; i < n; i++){
            for(int T = 0; T <= amount; T++){
                int  nottake = dp[i-1][T];
                int take = 1e9;
                if (coins[i] <= T) take = 1 + dp[i][T - coins[i]];
                dp[i][T] = min(take, nottake);
            }
        }
        int ans = dp[n - 1][amount];
        if (ans >= 1e9) return -1;
        return ans;
        */
        //By Recursion + DP + Memoization //Top Down
        //TC - O(n*amt) and SC - O(n*amt + n)
        /*
        int n = coins.size();
        vector<vector<int>> dp(n, vector<int> (amount+1, -1));
        int ans = solve(n - 1, coins, amount, dp);
        if (ans >= 1e9) return -1;
        return ans;
        */
    }
};