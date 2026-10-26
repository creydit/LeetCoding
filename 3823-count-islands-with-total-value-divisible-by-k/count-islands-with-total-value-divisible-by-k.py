class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        vis = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and grid[i][j] != 0:
                    total = 0
                    q = deque()
                    q.append((i,j))
                    vis[i][j] = 1
                    while q:
                        r,c = q.popleft()
                        total += grid[r][c]
                        for d in range(4):
                            rr = r + dx[d]
                            cc = c + dy[d]
                            if rr >= 0 and rr < n and cc >= 0 and cc < m and grid[rr][cc] != 0 and vis[rr][cc] == 0:
                                vis[rr][cc] = 1
                                q.append((rr,cc))
                    if total%k==0:
                        ans += 1
        return ans
