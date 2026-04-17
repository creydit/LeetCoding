class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:

        lcm = (r[0]*r[1]) // math.gcd(r[0],r[1]) 

        def solve(mid):
            s1 = mid - (mid//r[0])
            s2 = mid - (mid//r[1])
            ts = mid - (mid//lcm)
            return s1>=d[0] and s2>=d[1] and ts >= d[0]+d[1]

        lo = d[0]+d[1]
        hi = 2*lo*2
        ans = hi
        while lo <= hi:
            mid = (lo+hi)//2
            if solve(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans 