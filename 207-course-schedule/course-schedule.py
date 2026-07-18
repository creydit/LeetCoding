class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses+1)]

        for v,u in prerequisites:
            adj[u].append(v)

        vis = [0]*(numCourses+1)

        def dfs(node): 
            if vis[node] == 1:
                return True
            
            if vis[node] == 2:
                return False
            
            vis[node] = 1
            for nbr in adj[node]:
                if dfs(nbr):
                    return True
            
            vis[node] = 2
            return False

        for i in range(numCourses):
            if vis[i]==0:
                if dfs(i):
                    return False
        return True