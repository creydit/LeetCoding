class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        ans = n
        curr = 0
        for i in range(1,n):
            if prices[i]+1 == prices[i-1]:
                curr += 1
                ans += curr
            else:
                curr = 0
        return ans