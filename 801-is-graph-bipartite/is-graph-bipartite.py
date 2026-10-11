class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [0]*(n)
        for i in range(n):
            if color[i] != 0:
                continue
            q = deque()
            q.append(i)
            color[i] = 1
            while q:
                node = q.popleft()
                for nbr in graph[node]:
                    if color[nbr] == 0:
                        color[nbr] = 3 - color[node]
                        q.append(nbr)
                    elif color[nbr] == color[node]:
                        return False
        return True
            