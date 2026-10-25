class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for _ in range(n)]
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        for i in range(n):
            for j in range(m):
                if (i==0 or i==n-1 or j==0 or j == m-1) and grid[i][j] == 0:
                    q = deque()
                    q.append((i,j))
                    vis[i][j] = 1
                    while q:
                        r,c = q.popleft()
                        for d in range(4):
                            rr = r + dx[d]
                            cc = c + dy[d]
                            if rr >= 0  and rr < n and cc >= 0 and cc < m and grid[rr][cc] == 0 and vis[rr][cc] == 0:
                                q.append((rr,cc))
                                vis[rr][cc] = 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and grid[i][j] == 0:
                    ans += 1
                    q = deque()
                    q.append((i,j))
                    vis[i][j] = 1
                    while q:
                        r,c = q.popleft()
                        for d in range(4):
                            rr = r + dx[d]
                            cc = c + dy[d]
                            if rr >= 0 and rr < n and cc >= 0  and cc < m and grid[rr][cc] == 0 and vis[rr][cc] == 0:
                                vis[rr][cc] = 1
                                q.append((rr,cc))
        return ans
