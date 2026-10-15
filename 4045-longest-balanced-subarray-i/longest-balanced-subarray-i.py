class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            diff = 0
            for j in range(i,n):
                x = nums[j]
                if x not in seen:
                    seen.add(x)
                    if x%2==0:
                        diff+=1
                    else:
                        diff-=1
                if diff==0:
                    ans = max(ans,j-i+1)
        return ans
        