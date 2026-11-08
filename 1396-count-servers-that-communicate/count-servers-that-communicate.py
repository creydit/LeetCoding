class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        #Better
        #TC - O(N^2) and SC - (2N)
        n = len(grid)
        m = len(grid[0])
        rows = [0]*(n)
        cols = [0]*(m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        ans += 1
        return ans

        #Brute Force
        #Tc - O(n^3) SC - O(1)
        '''
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
        '''