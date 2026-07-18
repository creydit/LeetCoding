class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = defaultdict(list)
        for u in range(n):
            for v in range(n):
                if isConnected[u][v] == 1:
                    adj[u].append(v)
                    adj[v].append(u)

        vis = [0]*(n+1)
        def dfs(node):
            if vis[node] == 1:
                return
            vis[node] = 1
            for neigh in adj[node]:
                dfs(neigh)

        ans = 0
        for i in range(n):
            if vis[i] == 0:
                dfs(i)
                ans += 1
        return ans