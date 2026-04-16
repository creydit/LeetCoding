class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ''
        n = len(s)
        for i in range(n):
            for j in range(i):
                t = s[j:i+1]
                if set(t) == set(t.swapcase()):
                    ans = max(ans,t,key=len)
        return ans

