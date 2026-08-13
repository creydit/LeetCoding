class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def solve(s,op,cl):
            if op > n and cl > n:
                return
            if op==n and cl==n:
                ans.append(s)
                return 
            if op <= n:
                solve(s+'(',op+1,cl)
                if cl < op:
                    solve(s+')',op,cl+1)
            else:
                solve(s+')',op,cl+1)

        solve('(',1,0)
        return ans