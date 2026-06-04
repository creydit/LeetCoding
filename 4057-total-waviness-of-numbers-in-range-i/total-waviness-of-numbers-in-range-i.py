class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        #Brute Force
        # TC - O( ( num2 - num1 + 1) * d) where d = max number of digits in num2
        #here d = 5 as num2 <= 10^5 => 10000
        ans = 0
        for num in range(num1, num2+1):
            if num <= 99:
                continue
            s = str(num)
            n = len(s)
            peak = 0
            valley = 0
            for i in range(1,n-1):
                x = int(s[i-1])
                y = int(s[i])
                z = int(s[i+1])
                if y > x and y > z:
                    peak += 1
                elif y < x and y < z:
                    valley += 1
            ans += peak
            ans += valley
        return ans