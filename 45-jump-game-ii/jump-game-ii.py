class Solution:
    def jump(self, nums: List[int]) -> int:
        inf = 10**18
        n = len(nums)
        dp = [inf]*(n)
        dp[0] = 0
        for i in range(n):
            till = nums[i]
            for idx in range(1,till+1):
                if i+idx >= n: break
                dp[i+idx] = min(dp[i+idx], dp[i] + 1)
        return dp[n-1]