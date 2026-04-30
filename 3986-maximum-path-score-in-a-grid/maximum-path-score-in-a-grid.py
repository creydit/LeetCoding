class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        inf = float("-inf")
        dp = [[[inf]* (k+1) for _ in range(m)] for __ in range(n)]
        dp[0][0][0] = 0
        for i in range(n):
            for j in range(m):
                for c in range(k+1):
                    if dp[i][j][c] == inf:
                        continue
                    
                    if i < n-1:
                        val = grid[i+1][j]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i+1][j][c+cost] = max(dp[i+1][j][c+cost], dp[i][j][c] + val)
                    if j < m-1:
                        val = grid[i][j+1]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[i][j+1][c+cost] = max(dp[i][j+1][c+cost], dp[i][j][c] + val)
        ans = max(dp[n-1][m-1])
        return ans if ans >= 0 else -1