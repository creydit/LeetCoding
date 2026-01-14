class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])

        dr = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r,c,color,nc):
            if image[r][c] == color:
                return 
            
            image[r][c] = color
            for d in dr:
                rr = r + d[0]
                cc = c + d[1]
                if (rr>=0 and rr<n and cc>=0 and cc < m and image[rr][cc] == nc):
                    dfs(rr,cc,color,nc)

        dfs(sr,sc,color,image[sr][sc])
        return image 