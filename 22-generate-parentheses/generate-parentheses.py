class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def solve(s,o,c,n):
            if c > o or o > n or c > n:
                return 
            if o==c and o+c == 2*n:
                ans.append(s)
                return

            solve(s+'(',o+1,c,n)
            solve(s+')',o,c+1,n)

        solve('(',1,0,n)
        return ans 