class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        ans = 0
        for i in costs:
            if i > coins:
                break
            else:
                ans += 1
                coins -= i
        return ans
        