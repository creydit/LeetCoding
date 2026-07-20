class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j])
        nn = n*m
        for _ in range(k):
            arr = [arr[-1]] + arr[:n*m-1]
        ans = []
        idx = 0
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(arr[idx])
                idx += 1
            ans.append(temp)
        return ans