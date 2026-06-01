class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort()
        ans = 0
        candies = 0
        for i in range(n-1,-1,-1):
            if candies == 2:
                candies = 0
                continue
            ans += cost[i]
            candies += 1
        return ans 