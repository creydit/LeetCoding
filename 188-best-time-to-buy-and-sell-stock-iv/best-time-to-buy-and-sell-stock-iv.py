class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*(k+1) for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for t in range(k-1,-1,-1):
                dp[i][0][t] = max(dp[i+1][0][t], -prices[i] + dp[i+1][1][t])
                dp[i][1][t] = max(dp[i+1][1][t], prices[i] + dp[i+1][0][t+1])
        return dp[0][0][0]