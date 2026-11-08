class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        #Optimal
        #TC - O(N^2) and SC- O(1)
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            servers = 0
            idx = -1
            for j in range(m):
                if grid[i][j] == 1:
                    servers += 1
                    idx = j
            if servers > 1:
                ans += servers
            elif servers == 1:
                for r in range(n):
                    if r != i and grid[r][idx] == 1:
                        ans += 1
                        break
        return ans

        #Better
        #TC - O(N^2) and SC - (2N)
        '''
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
        '''

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