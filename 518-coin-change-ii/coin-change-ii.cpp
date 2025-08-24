class Solution {
public:
    /*
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
    */
    int change(int amount, vector<int>& coins) {
        //By coin change logic instead if just calculating money we just count it in 
        
        //Space Optimised
        //TC - O(n*amount) and SC - O(2amount)
        using u128 = unsigned __int128;
        int n = coins.size();
        vector<u128> prev(amount+1 , 0), curr(amount+1, 0);
        for(int target = 0; target <= amount; target++){
            if (target % coins[0] == 0) prev[target] = 1;
        }
        for(int idx = 1; idx < n; idx++){
            for(int target = 0; target <= amount; target++){
                u128 nottake = prev[target];
                u128 take = 0;
                if (coins[idx] <= target) take = curr[target - coins[idx]];
                curr[target] = take + nottake;
            }
            prev = curr;
        }
        return (int)prev[amount];

        //By Tabultion
        //TC - O(n*amount) and SC - O(n*amount)
        /*
        using u128 = unsigned __int128;
        int n = coins.size();
        vector<vector<u128>> dp(n, vector<u128>(amount+1, 0));
        for(int target = 0; target <= amount; target++){
            if (target % coins[0] == 0) dp[0][target] = 1;
        }
        for(int idx = 1; idx < n; idx++){
            for(int target = 0; target <= amount; target++){
                u128 nottake = dp[idx - 1][target];
                u128 take = 0;
                if (coins[idx] <= target) take = dp[idx][target - coins[idx]];
                dp[idx][target] = take + nottake;
            }
        }
        return (int)dp[n-1][amount];
        */

        //1 way to apporach answer
        //By Recursion + DP + memoization
        //TC - O(n*amount) and SC - O(n*amount + n)
        /*
        int n = coins.size();
        vector<vector<int>> dp(n, vector<int>(amount+1, -1));
        return solve(n-1, coins, amount, dp);
        */
    }
};