class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        curr = 0
        for i in nums:
            if i==1:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 0
        return ans
        