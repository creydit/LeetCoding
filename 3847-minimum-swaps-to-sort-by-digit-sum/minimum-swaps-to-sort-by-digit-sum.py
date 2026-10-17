class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        def digSum(x):
            ss = 0
            for i in str(x):
                ss += int(i)
            return ss
        arr = sorted(nums, key = lambda x: (digSum(x), x))
        pos = {}
        for i in range(n):
            pos[arr[i]] = i
        ans = 0
        vis = [0]*n
        for i in range(n):
            if vis[i] or pos[nums[i]] == i:
                continue
            j = i
            cnt = 0
            while not vis[j]:
                vis[j] = 1
                j = pos[nums[j]]
                cnt += 1
            ans += cnt-1
        return ans