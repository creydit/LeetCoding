class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero.append((i,j))
        for i,j in zero:
            for k in range(i):
                matrix[k][j] = 0
            for k in range(i+1,n):
                matrix[k][j] = 0
            for k in range(j):
                matrix[i][k] = 0
            for k in range(j+1,m):
                matrix[i][k] = 0