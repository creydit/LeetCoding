class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        #Math
        if target > x+y:
            return False
        g = math.gcd(x,y)
        if target%g==0:
            return True
        return False