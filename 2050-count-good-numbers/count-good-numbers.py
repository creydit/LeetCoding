class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        def po(x,n):
            if x==1 or n==0:
                return 1
            if n==1:
                return x%mod
            if n%2==1:
                return x*po(x%mod,n-1)
            return po(x*x % mod,n//2)

        even = (n+1)//2
        odd = n//2
        ans = (po(5,even) * po(4,odd)) % mod
        return ans