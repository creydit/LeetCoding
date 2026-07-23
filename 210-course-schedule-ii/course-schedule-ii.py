class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        vis = [0]*(numCourses)
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)

        ans = []
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
            ans.append(node)
            return False

        for i in range(numCourses):
            if not vis[i]:
                if dfs(i):
                    return []
        return ans[::-1]