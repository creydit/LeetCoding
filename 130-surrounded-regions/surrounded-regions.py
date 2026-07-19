class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        vis = [[0]*m for _ in range(n)]        
        q = deque()

        for i in range(n):
            if board[i][0] == 'O':
                vis[i][0] = 1
                q.append((i,0))
            if board[i][m-1] == 'O':
                vis[i][m-1] = 1
                q.append((i,m-1))

        for j in range(m):
            if board[0][j] == 'O':
                vis[0][j] = 1
                q.append((0,j))
            if board[n-1][j] == 'O':
                vis[n-1][j] = 1
                q.append((n-1,j))
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while q:
            r,c = q.popleft()
            for d in range(4):
                rr = r + dx[d]
                cc = c + dy[d]
                if rr>=0 and rr < n and cc>0 and cc < m and vis[rr][cc]==0 and board[rr][cc] == 'O':
                    vis[rr][cc] = 1
                    q.append((rr,cc))

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and vis[i][j]==0:
                    board[i][j] = 'X'
    