class Solution:
    def countAnagrams(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        fact = [1]*(n+1)
        for i in range(1,n+1):
            fact[i] = fact[i-1]*i % mod
        
        invfact = [1]*(n+1)
        invfact[n] = pow(fact[n], mod-2, mod)
        for i in range(n,0,-1):
            invfact[i-1] = invfact[i]*i % mod
        ans = 1
        for word in s.split():
            freq = [0]*26
            for c in word:
                freq[ord(c) - ord('a')] += 1   
            nn = fact[len(word)]
            for f in freq:
                nn = nn * invfact[f] % mod
            ans = ans* nn % mod
        return ans
