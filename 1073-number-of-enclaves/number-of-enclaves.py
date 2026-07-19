class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        vis = [[0]*m for _ in range(n)]

        for i in range(n):
            if grid[i][0] == 1:
                vis[i][0] = 1
                q.append((i,0))
            if grid[i][m-1] == 1:
                vis[i][m-1] = 1
                q.append((i,m-1))
        for j in range(m):
            if grid[0][j] == 1:
                vis[0][j] = 1
                q.append((0,j))
            if grid[n-1][j] == 1:
                vis[n-1][j] = 1
                q.append((n-1,j))
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while q:
            r,c = q.popleft()
            for d in range(4):
                rr = r + dx[d]
                cc = c + dy[d]

                if rr>=0 and rr<n and cc>=0 and cc<m and vis[rr][cc] == 0 and grid[rr][cc] == 1:
                    vis[rr][cc] = 1
                    q.append((rr,cc))
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    ans += 1
        return ans