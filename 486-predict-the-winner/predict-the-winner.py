class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0]*21 for _ in range(22)]
        n = len(nums)
        for i in range(n):
            dp[i][i] = nums[i]
        
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                dp[i][j] = max( nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        
        return dp[0][n-1] >= 0