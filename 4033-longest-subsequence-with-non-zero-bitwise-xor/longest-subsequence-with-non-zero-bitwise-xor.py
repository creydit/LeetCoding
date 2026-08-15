class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in nums:
            xor ^= i
        if xor!=0:
            return n
        if len(set(nums))==1 and nums[0]==0:
            return 0
        return n-1