class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        vis = [0]*(n+1)
        adj = defaultdict(list)
        for u,v,c in roads:
            adj[u].append((v,c))
            adj[v].append((u,c))
        q = deque()
        q.append(1)
        vis[1] = 1
        ans = 10**18
        while q:
            node = q.popleft()
            for neigh,cost in adj[node]:
                ans = min(ans,cost)
                if vis[neigh]==0:
                    vis[neigh] = 1
                    q.append(neigh)
        return ans


