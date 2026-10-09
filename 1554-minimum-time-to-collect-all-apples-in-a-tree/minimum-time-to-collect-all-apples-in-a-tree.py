class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        time = 0
        def dfs(node, par):
            nonlocal time
            haveA = hasApple[node]
            for nbr in adj[node]:
                if nbr != par:
                    hA = dfs(nbr, node)
                    if hA:
                        time += 2
                    haveA |= hA
            return haveA
        dfs(0,-1)
        return time
