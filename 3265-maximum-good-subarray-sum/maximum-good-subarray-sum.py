class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = defaultdict(int)
        ans = -10**18
        pref = 0
        for i in range(n):
            x = nums[i]
            curr = pref + x
            if x+k in dic:
                ans = max(ans, curr - dic[x+k])
            if x-k in dic:
                ans = max(ans, curr - dic[x-k])
            if x not in dic:
                dic[x] = pref
            else:
                dic[x] = min(dic[x], pref)
            pref = curr

        if ans == -10**18:
            return 0
        return ans