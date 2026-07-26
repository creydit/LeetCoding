class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        ans = 0
        for i in range(1,n):
            profit = prices[i] - buy
            if profit < 0:
                buy = prices[i]
            else:
                ans = max(ans,profit)
        return ans











        '''

        profit = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            cost = prices[i] - mini
            profit = max(profit, cost)
            mini = min(mini, prices[i])
        return profit
        '''