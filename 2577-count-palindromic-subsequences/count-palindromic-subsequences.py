class Solution:
    def countPalindromes(self, s: str) -> int:
        mod = 10**9+7
        n = len(s)

        left = [0]*(10)
        right = [0]*(10)
        leftPair = [[0]*10 for __ in range(10)]
        rightPair = [[0]*10 for __ in range(10)]
        
        for i in range(n-1,-1,-1):
            x = int(s[i])
            for b in range(10):
                rightPair[x][b] += right[b]
            right[x] += 1

        ans = 0

        for i in range(n):
            x = int(s[i])

            right[x] -= 1
            for b in range(10):
                rightPair[x][b] -= right[b]

            for a in range(10):
                for b in range(10):
                    ans += leftPair[a][b] * rightPair[b][a] 
            
            for a in range(10):
                leftPair[a][x] += left[a]
            left[x] += 1

        return ans%mod
