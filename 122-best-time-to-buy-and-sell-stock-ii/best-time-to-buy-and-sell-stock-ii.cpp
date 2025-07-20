class Solution {
public:
    long long solve(int idx, int buy, vector<int> &prices, vector<vector<int>> &dp){
        if( idx == prices.size()) return 0;
        if(dp[idx][buy] != -1) return dp[idx][buy];
        long long profit = 0;
        if(buy){
            profit = max( - prices[idx] + solve(idx + 1, 0, prices, dp),
                            0 + solve(idx + 1, 1, prices, dp));
        }
        else{
            profit = max( prices[idx] + solve(idx + 1, 1, prices, dp),
                            0 + solve(idx + 1, 0, prices, dp));
        }
        return dp[idx][buy] = profit;
    }
    int maxProfit(vector<int>& prices) {
        //BY Dp and memoization 
        //Top down
        //TC - O(n*2) and SC - O(2*n = n)
        int n = prices.size();
        vector<vector<int>> dp(n, vector<int> (2, -1));
        return solve(0, 1, prices, dp);
    }
};