class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])
        vis = [[-1 for _ in range(m)] for __ in range(n)]
        if grid[0][0] == 1:
            health -= 1
        if health < 1:
            return False
        q = deque()
        q.append((0,0,health))
        vis[0][0] = health
        dx = [0,1,-1,0]
        dy = [-1,0,0,1]
        while q:
            r,c,h = q.popleft()
            if r == n-1 and c==m-1:
                return True
            for d in range(4):
                rr = r + dx[d]
                cc = c + dy[d]
                if rr>=0 and rr<n and cc>=0 and cc<m:
                    nh = h - grid[rr][cc]
                    if nh>0 and nh>vis[rr][cc]:
                        vis[rr][cc] = nh
                        q.append((rr,cc,nh))
        return False