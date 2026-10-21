class Solution:
    def isPossible(self, n: int, edges: list[list[int]]) -> bool:
        adj = [set() for _ in range(n+1)]
        degree = [0]*(n+1)
        
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1

        odd = []
        for i in range(1,n+1):
            if degree[i]%2==1:
                odd.append(i)

        nn = len(odd)

        if nn == 0:
            return True

        if nn == 2:
            a,b = odd
            if b not in adj[a]:
                return True
            for c in range(1,n+1):
                if c != a and c != b:
                    if c not in adj[a] and c not in adj[b]:
                        return True
            return False

        if nn == 4:
            a,b,c,d = odd
            if b not in adj[a] and d not in adj[c]:
                return True
            if c not in adj[a] and b not in adj[d]:
                return True
            if d not in adj[a] and c not in adj[b]:
                return True
            return False

        return False
        