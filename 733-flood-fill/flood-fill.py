class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        n = len(image)
        m = len(image[0])
        oldc = image[sr][sc]
        if oldc == color:
            return image
        q = deque()
        q.append((sr,sc))
        image[sr][sc] = color
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        while q:
            r,c = q.popleft()
            for d in range(4):
                rr = r + dx[d]
                cc = c + dy[d]
                if 0 <= rr < n and 0 <= cc < m and image[rr][cc] == oldc:
                    q.append((rr,cc))
                    image[rr][cc] = color
        return image
                
