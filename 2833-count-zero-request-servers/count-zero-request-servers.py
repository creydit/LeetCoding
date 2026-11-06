class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        ans = [0]*(len(queries))
        cnt = [0]*(n+1)
        logs.sort(key = lambda x : x[1])
        ids = sorted(range(len(queries)), key = lambda i : queries[i])
        l = r = a = 0
        for i in ids:
            q = queries[i]
            while r < len(logs) and logs[r][1] <= q:
                id = logs[r][0]
                if cnt[id] == 0:
                    a += 1
                cnt[id] += 1
                r += 1
            while l < r and logs[l][1] < q-x:
                id = logs[l][0]
                cnt[id] -= 1
                if cnt[id] == 0:
                    a -= 1
                l += 1
            ans[i] = n - a
        return ans