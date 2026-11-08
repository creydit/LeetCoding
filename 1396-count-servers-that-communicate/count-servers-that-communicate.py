class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ok = False
                    for r in range(i):
                        if grid[r][j] == 1:
                            ok = True
                            break
                    for r in range(i+1,n):
                        if grid[r][j] == 1:
                            ok = True
                            break
                    for c in range(j):
                        if grid[i][c] == 1:
                            ok = True
                            break
                    for c in range(j+1,m):
                        if grid[i][c] == 1:
                            ok = True
                            break
                    if ok:
                        ans += 1
        return ans