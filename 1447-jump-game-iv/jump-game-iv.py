class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #MY BFS
        n = len(arr)
        dic = defaultdict(list)
        for i in range(n):
            dic[arr[i]].append(i)
        vis = [0]*(n+1)

        q = deque()
        q.append((0,0))
        vis[0] = 1
        ans = 10**18
        while q:
            node = q.popleft()
            at = node[0]
            jumps = node[1]
            if at == n-1:
                return jumps

            m1 = at + 1
            if m1 < n and vis[m1] == 0:
                q.append((m1,jumps+1))
                vis[m1] = 1

            m2 = at - 1
            if m2 >= 0 and vis[m2] == 0:
                q.append((m2,jumps+1))
                vis[m2] = 1
            

            for m in dic[arr[at]]:
                if m != at:
                    m3 = m
                    if vis[m3] == 0:
                        q.append((m3,jumps+1))
                        vis[m3] = 1
            dic[arr[at]] = []
        return 0
            