class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1 for _ in range(m)] for __ in range(n)]

        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                else:
                    up = grid[i][j] 
                    if j > 0:
                        up += dp[i][j-1]
                    else:
                        up = 1e9
                    
                    left = grid[i][j]
                    if i > 0:
                        left += dp[i-1][j]
                    else:
                        left = 1e9
                    dp[i][j] = min(up,left)
                
        '''
        def solve(r, c):
            if r == n-1 and c == m-1:
                return grid[r][c]
            
            if r >= n or c >= m:
                return 1e9
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            dp[r][c] = grid[r][c] + min(solve(r+1,c), solve(r,c+1))
            return dp[r][c]
        '''
        ans = dp[n-1][m-1]
        return ans 