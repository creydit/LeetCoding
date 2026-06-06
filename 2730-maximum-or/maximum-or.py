class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0]*n
        suff = [0]*n
        pref[0] = nums[0]
        for i in range(1,n):
            pref[i] = pref[i-1] | nums[i]
        suff[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suff[i] = suff[i+1] | nums[i]
        
        ans = 0
        for i in range(n):
            left = pref[i-1] if i>0 else 0
            right = suff[i+1] if i<n-1 else 0

            ans = max(ans, left | nums[i] << k | right)
        
        return ans