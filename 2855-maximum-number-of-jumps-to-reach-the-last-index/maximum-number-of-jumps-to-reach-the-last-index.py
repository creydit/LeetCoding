class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1]*n
        dp[0] = 0
        for i in range(n):
            for j in range(i+1,n):
                if dp[i]!= -1 and abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j],dp[i]+1)
        return dp[n-1]
        '''
        n = len(nums)
        ans = 0
        i = 0
        j = 1
        while i < n and j < n:
            if abs(nums[j] - nums[i]) <= target:
                ans += 1
                i = j
                j += 1
            else:
                j += 1
        if i==n-1:
            return ans 
        return -1
        '''