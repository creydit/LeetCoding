class Solution:
    def countSubstrings(self, s: str) -> int:
        #dp
        n = len(s)
        dp = [[False]*(n+1) for _ in range(n+1)]
        ans = 0

        for i in range(n):
            dp[i][i] = 1
            ans += 1
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    ans += 1
        return ans 

        #brute force
        '''
        def isP(c):
            n = len(c)
            for i in range(n//2):
                if c[i] == c[n-1-i]:
                    continue
                return False
            return True

        n = len(s)
        substr = []
        for i in range(n):
            for j in range(i,n):
                substr.append(s[i:j+1])
        ans = 0
        for c in substr:
            if isP(c):
                ans += 1
        return ans     
        '''