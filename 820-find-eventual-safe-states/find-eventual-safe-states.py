class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0]*n
        def dfs(node):
            if vis[node] == 1:
                return True
            if vis[node] == 2:
                return False
            
            vis[node] = 1
            for nbr in graph[node]:
                if dfs(nbr):
                    return True
            vis[node] = 2
            return False

        for i in range(n):
            if vis[i]==0:
                dfs(i)

        ans = []
        for i in range(n):
            if vis[i]!=1:
                ans.append(i)
        return ans