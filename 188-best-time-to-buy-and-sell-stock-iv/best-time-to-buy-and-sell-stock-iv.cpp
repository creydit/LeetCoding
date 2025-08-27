class Solution {
public:
    int solve(int idx, int trans, vector<int>& prices, int n, int k, vector<vector<int>> &dp){
        if (idx == n || trans == 2*k ) return 0;

        if(dp[idx][trans] != -1) return dp[idx][trans];
        int profit = 0;
        if (trans%2 == 0){
            profit = max( -prices[idx] + solve(idx+1, trans + 1, prices, n, k, dp), 
                            0 + solve(idx+1, trans, prices, n ,k, dp));
        }
        else{
            profit = max( prices[idx] + solve(idx+1, trans + 1, prices, n, k, dp),
                            0 + solve(idx + 1, trans, prices, n, k, dp));
        }
        return dp[idx][trans] = profit;

    }
    int maxProfit(int k, vector<int>& prices) {
        //similar problem to buy and sell stocks 3 just there were only two transactions allowed 
        //here we have k allowed transactions

        //Solving with another approach which is using transaction number that will be even for buying
        //and odd for selling 
        // TC - O(n*2k) and SC - O(n*2k + n)
        int n = prices.size();
        vector<vector<int>> dp(n , vector<int> (2*k, -1));
        return solve(0, 0, prices, n, k, dp);


        //solving direct space optimsied version //refer BAS3 for more detials
        //TC - (n*2*k) and SC - O(2*k)
        /*
        int n = prices.size();
        vector<vector<int>> ahead(2, vector<int>(k+1, 0));
        vector<vector<int>> curr(2, vector<int>(k+1, 0));

        for(int idx = n-1; idx >= 0; idx--){
            for(int buy = 0; buy <= 1; buy++){
                for(int cap = 1; cap <= k; cap++){
                    int profit = 0;
                    if (buy){
                        profit = max( -prices[idx] + ahead[0][cap], 0 + ahead[1][cap]);
                    }
                    else{
                        profit = max(prices[idx] + ahead[1][cap-1], 0 + ahead[0][cap]);
                    }
                    curr[buy][cap] = profit;
                }
            }
            ahead = curr;
        }
        return ahead[1][k];
        */

    }
};