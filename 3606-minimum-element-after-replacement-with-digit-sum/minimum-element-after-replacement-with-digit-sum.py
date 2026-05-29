class Solution:
    def minElement(self, nums: List[int]) -> int:
        def ds(n):
            ss = 0
            while n > 0:
                ss += n%10
                n//=10
            return ss
        
        ans = 10**18
        for i in nums:
            ans = min(ans, ds(i))
        
        return ans