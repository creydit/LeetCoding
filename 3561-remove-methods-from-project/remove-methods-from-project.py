class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u,v in invocations:
            adj[u].append(v)

        buggy = [0]*(n)

        def dfs1(node):
            buggy[node] = 1
            for nbr in adj[node]:
                if buggy[nbr] == 0:
                    dfs1(nbr)

        buggy[k] = 0
        dfs1(k)
        vis = [0]*(n)
        remove = buggy.copy()

        def dfs2(node):
            vis[node] = 1
            remove[node] = 0
            for nbr in adj[node]:
                if vis[nbr] == 0:
                    dfs2(nbr)
            
        for node in range(n):
            if buggy[node] == 0 and vis[node] == 0:
                dfs2(node)

        every = False
        ans = []
        for i in range(n):
            if buggy[i] == 1 and remove[i] == 0:
                every = True
                break
            elif remove[i] == 0:
                ans.append(i)
        if every:
            return [i for i in range(n)]
        return ans