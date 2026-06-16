class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        #tabulation more natural 
        n = len(nums)
        dp = [[float('-inf')]*(target + 1) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(1,n+1):
            for t in range(target+1):
                dp[i][t] = dp[i-1][t]

                if t >= nums[i-1]:
                    dp[i][t] = max(dp[i][t], dp[i-1][t-nums[i-1]] + 1)

        ans = dp[n][target]
        return ans if ans > 0 else -1


        #Memoization
        '''
        n = len(nums)
        dp = [[-1]*(target+1) for _ in range(n+1)]
        def solve(idx, runsum):
            if runsum == target:
                return 0

            if idx == n or runsum > target:
                return float('-inf')

            if dp[idx][runsum] != -1:
                return dp[idx][runsum]

            nottake = solve(idx+1, runsum)
            take = 1 + solve(idx+1, runsum + nums[idx])

            dp[idx][runsum] = max(take, nottake)
            
            return dp[idx][runsum]
        
        ans = solve(0,0)
        return ans if ans > 0 else -1
        '''
            