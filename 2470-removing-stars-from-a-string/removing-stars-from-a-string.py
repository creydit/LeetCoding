class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        ans=''
        for i in range(n):
            if s[i] != '*':
                ans += s[i]
            else:
                if ans:
                    ans = ans[:-1]        
        return ans