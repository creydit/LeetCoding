class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        good = 0
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    good += 1
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while q:
            r,c,time = q.popleft()
            ans = max(ans, time)
            for d in range(4):
                rr = r + dx[d]
                cc = c + dy[d]
                if rr >= 0 and rr < n and cc >= 0 and cc < m and grid[rr][cc] == 1:
                    good -= 1
                    grid[rr][cc] = 2
                    q.append((rr,cc,time+1))
        if good == 0:
            return ans
        return -1