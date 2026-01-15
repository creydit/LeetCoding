class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        ans = 10**18
        s = 0
        while r<n:

            s += nums[r]
             
            while s >= target:
                ans = min(ans, r-l+1)
                s -= nums[l]
                l+=1
            
            r += 1

        return ans if ans!=10**18 else 0