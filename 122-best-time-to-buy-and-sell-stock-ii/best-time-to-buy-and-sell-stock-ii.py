class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        for i in range(1,n):
            ans += max(0, prices[i] - prices[i-1])
        return ans