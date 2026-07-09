class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        #TC - O(n+q) and SC - O(n)
        comps = [0]*(n)
        for i in range(1,n):
            if nums[i]-nums[i-1] <= maxDiff:
                comps[i] = comps[i-1]
            else:
                comps[i] = comps[i-1]+1
        ans = [False]*len(queries)
        for i in range(len(queries)):
            u=queries[i][0]
            v=queries[i][1]
            if comps[u] == comps[v]:
                ans[i] = True
        return ans