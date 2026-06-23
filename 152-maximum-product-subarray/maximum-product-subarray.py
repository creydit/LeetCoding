class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -10**18
        prod = 1
        for i in range(n):
            prod*=nums[i]
            ans = max(ans,prod)
            if prod==0:
                prod=1
        prod = 1
        for i in range(n-1,-1,-1):
            prod*=nums[i]
            ans = max(ans,prod)
            if prod==0:
                prod = 1
        return ans 
