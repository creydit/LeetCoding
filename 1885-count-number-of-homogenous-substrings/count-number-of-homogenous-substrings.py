class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 1000000007
        n = len(s)
        ans = 1
        curr = 1
        for i in range(1,n):
            if s[i] == s[i-1]:
                curr += 1
            else:
                curr = 1
            ans = (ans + (curr%mod))%mod
        return ans