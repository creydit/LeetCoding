class Solution:
    def generate(self, numRows: int) -> List[List[int]]:  
        def solve(n):
            ans = 1
            arr = [1]
            for i in range(1,n):
                ans *= n - i
                ans //= i
                arr.append(ans)
            return arr          
        ans = []
        for i in range(1,numRows+1):
            ans.append(solve(i))
        return ans

        