class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

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
            
            