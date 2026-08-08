class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        #by DFS
        if target > x+y:
            return False
        seen = set()
        def dfs(total):
            if total == target:
                return True
            if total in seen or total < 0 or total > x+y:
                return False
            seen.add(total)
            op1 = dfs(total+x)
            op2 = dfs(total-x)
            op3 = dfs(total+y)
            op4 = dfs(total-y)
            return op1 or op2 or op3 or op4
        return dfs(0)

        #Math
        '''
        if target > x+y:
            return False
        g = math.gcd(x,y)
        if target%g==0:
            return True
        return False
        '''