class Solution {
public: 
    /*
    int solve(int idx, int buy, vector<int>& prices, vector<vector<int>>& dp){
        if (idx >= prices.size()) return 0;

        if (dp[idx][buy] != -1) return dp[idx][buy];
        int profit = 0;
        if (buy){
            profit = max( -prices[idx] + solve(idx+1, 0, prices, dp),
                            0  + solve(idx+1, 1, prices, dp));
        }
        else{
            profit = max( prices[idx] + solve(idx + 2, 1, prices, dp),
                            0 + solve(idx + 1, 0, prices, dp));
        }

        return dp[idx][buy] = profit;
    }
    */
    int maxProfit(vector<int>& prices) {
        //almost same as buy and sell stock 2 with only difference of cooldown which can be
        //done by skipping 1 index after selling 
        
        //Space OPtimisation
        // TC - O(2*n) and SC - O(6)
        int n = prices.size();
        vector<int> f2(2, 0);
        vector<int> f1(2, 0);
        vector<int> curr(2, 0);

        for(int idx = n-1; idx >= 0; idx--){
            for(int buy = 0; buy <= 1; buy++){
                int profit = 0;
                if (buy){
                    profit = max( -prices[idx] + f1[0],
                                    0  + f1[1] );
                }
                else{
                    profit = max( prices[idx] + f2[1],
                                    0 + f1[0] );
                }

                curr[buy] = profit;
            }
            f2 = f1;
            f1 = curr;
        }
        return f1[1];
        
        
        //by tabulation
        // TC - O(2*n) and SC - O(2*n)
        /*
        int n = prices.size();
        vector<vector<int>> dp(n+2, vector<int>(2, 0));

        for(int idx = n-1; idx >= 0; idx--){
            for(int buy = 0; buy <= 1; buy++){
                int profit = 0;
                if (buy){
                    profit = max( -prices[idx] + dp[idx+1][0],
                                    0  + dp[idx+1][1] );
                }
                else{
                    profit = max( prices[idx] + dp[idx + 2][1],
                                    0 + dp[idx + 1][0] );
                }

                dp[idx][buy] = profit;
            }
        }
        return dp[0][1];
        */

        //by Recursion + DP + memoization
        // TC - O(2*n) and SC - O(2*n + n)
        /*
        int n = prices.size();
        vector<vector<int>> dp(n+1, vector<int>(2, -1));
        return solve(0, 1, prices, dp);
        */
    }
};