class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        #better but with space
        mod = 1000000007
        n = len(nums)
        idx1 = []
        for i in range(n):
            if nums[i] == 1:
                idx1.append(i)
        ans = 1
        for i in range(1,len(idx1)):
            ans *= (idx1[i] - idx1[i-1])

        if len(idx1) == 0:
            return 0
        return ans%mod
