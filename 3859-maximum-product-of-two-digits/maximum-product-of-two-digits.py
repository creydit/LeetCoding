class Solution:
    def maxProduct(self, n: int) -> int:
        mx = -1
        mx2 = -1
        for i in str(n):
            val = int(i)
            if val > mx:
                mx2 = mx
                mx = val
            elif val > mx2:
                mx2 = val
        return mx*mx2