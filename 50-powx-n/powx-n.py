class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(x,n):
            if x==1 or n==0:
                return 1
            if n==1:
                return x
            if n%2==1:
                return x*solve(x,n-1)
            return solve(x*x,n//2)
        if n < 0:
            return 1/solve(x, -n)
        return solve(x,n)
        '''
        nn = n
        ans = 1
        if nn < 0 :
            nn = -1*nn
        while nn:
            if nn%2==1:
                ans = ans*x
                nn -= 1
            else:
                x = x*x
                nn = nn//2
        if n < 0:
            ans = 1 / ans
        return ans
        '''
        