class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        inf = 10**9
        n = len(triangle)
        dp = [ [inf for __ in range(n)] for _ in range(n)]

        dp[0][0] = triangle[0][0]

        for i in range(1,n):
            for j in range(i+1):
                if j==0:
                    dp[i][j] = dp[i-1][0] + triangle[i][0]
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        
        return min(dp[n-1])