class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        costs.sort()
        ans = 0
        for i in range(n):
            if coins >= costs[i]:
                ans += 1
                coins -= costs[i]
            else:
                break
        return ans