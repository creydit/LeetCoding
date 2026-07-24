class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        ss = sum(nums)
        if ss%2==1:
            return False
        target = ss//2
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(n):
            for sums in range(target,0,-1):
                if sums - nums[i] >= 0:
                    dp[sums] = (dp[sums] or dp[sums - nums[i]])
        return dp[target]==1
