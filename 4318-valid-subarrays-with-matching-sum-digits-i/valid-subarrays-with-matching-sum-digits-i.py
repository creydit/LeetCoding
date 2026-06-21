class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        #Brute Force
        #TC - O(n^2)
        ans = 0
        n = len(nums)
        for i in range(n):
            ss = 0
            for j in range(i,n):
                ss += nums[j]
                s = str(ss)
                if int(s[0]) == x and int(s[-1]) == x:
                    ans += 1
        return ans 