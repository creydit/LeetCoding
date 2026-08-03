class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        zeroes= 0
        ans = 0
        l = 0
        for r in range(n):
            if nums[r] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans