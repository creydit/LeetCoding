class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        q = deque()
        vis = [[0]*m for _ in range(n)]

        for r,c,color in sources:
            vis[r][c] = color
            q.append((r,c,color))

        while q:
            size = len(q)
            temp = defaultdict(int)
            for _ in range(size):
                r, c, color = q.popleft()

                for d in range(4):
                    rr = r + dx[d]
                    cc = c + dy[d]

                    if (0 <= rr < n and 0 <= cc < m and vis[rr][cc] == 0):
                        temp[(rr, cc)] = max(temp[(rr, cc)], color)

            for (r, c), color in temp.items():
                vis[r][c] = color
                q.append((r, c, color))

        return vis