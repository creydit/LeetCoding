class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0]*n

        def dfs(node, temp):
            if vis[node]:
                return 

            vis[node] = 1
            temp.append(node)
            for neighbour in adj[node]:
                dfs(neighbour,temp)

        components = []
        for i in range(n):
            if vis[i] == 0:
                temp = []
                dfs(i, temp)
                components.append(temp)

        ans = 0
        for comp in components:
            numOfV = len(comp)
            numOfE = 0
            for u in comp:
                numOfE += len(adj[u])
            numOfE = numOfE//2
            totE = (numOfV * (numOfV - 1))//2
            if numOfE == totE:
                ans += 1
        return ans




        