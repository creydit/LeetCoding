class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        //similar problem to buy and sell stocks 3 just there were only two transactions allowed 
        //here we have k allowed transactions

        //solving direct space optimsied version //refer BAS3 for more detials
        //TC - (n*2*k) and SC - O(2*k)
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

    }
};