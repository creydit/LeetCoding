class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            dp[i] = -10**18
            op1 = stoneValue[i] - dp[i+1]
            dp[i] = max(dp[i],op1)
            if i+1 < n:
                op2 = stoneValue [i] + stoneValue[i+1] - dp[i+2]
                dp[i] = max(dp[i],op2)
            if i+2<n:
                op3 = stoneValue [i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3]
                dp[i] = max(dp[i],op3)
        if dp[0] == 0:
            return "Tie"
        if dp[0] > 0 :
            return "Alice"
        return "Bob"