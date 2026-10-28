class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0]*1024 for __ in range(m)] for _ in range(n)]

        dp[0][0][grid[0][0]] = 1
        for i in range(1,n):
            for v in range(1024):
                dp[i][0][v] = dp[i-1][0][v^grid[i][0]]
        for j in range(1,m):
            for v in range(1024):
                dp[0][j][v] = dp[0][j-1][v^grid[0][j]]
        
        for i in range(1,n):
            for j in range(1,m):
                for v in range(1024):
                    op1 = dp[i-1][j][v ^ grid[i][j]]
                    op2 = dp[i][j-1][v ^ grid[i][j]]
                    dp[i][j][v] = op1 | op2

        for i in range(1024):
            if dp[n-1][m-1][i] == 1:
                return i

        return -1
        

