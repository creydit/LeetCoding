class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1 for _ in range(m)] for __ in range(n)]

        def solve(r, c):
            if r == n-1 and c == m-1:
                return grid[r][c]
            
            if r >= n or c >= m:
                return 1e9
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            dp[r][c] = grid[r][c] + min(solve(r+1,c), solve(r,c+1))
            return dp[r][c]
        
        ans = solve(0,0)
        return ans 