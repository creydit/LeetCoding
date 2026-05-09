class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
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


        '''
        #Better - Brute Force
        #O(n2)
        n = len(nums)
        ans = 0
        for i in range(n):
            evens = set()
            odds = set()
            for j in range(i,n):
                if nums[j]%2==0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])
                if len(evens)==len(odds):
                    ans = max(ans, j-i+1)
        return ans
        '''