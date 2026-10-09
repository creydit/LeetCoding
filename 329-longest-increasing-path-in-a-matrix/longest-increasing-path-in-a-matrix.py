class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        dp = [[0]*m for _ in range(n)]

        def dfs(sr,sc):
            if dp[sr][sc] != 0:
                return dp[sr][sc]
            best = 0
            for d in range(4):
                rr = sr + dx[d]
                cc = sc + dy[d]
                if rr >=0 and rr < n and cc >=0 and cc < m and matrix[rr][cc] > matrix[sr][sc]:
                    best = max(best,dfs(rr,cc))
            dp[sr][sc] = 1+best
            return dp[sr][sc]
            
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i,j))
        return ans