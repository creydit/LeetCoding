class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n = len(text)
        hash = [0]*26
        for i in text:
            hash[ord(i) - ord('a')] += 1
        
        ans = 10**18
        for i in "balon":
            if i=='l' or i=='o':
                ans = min(ans, hash[ord(i) - ord('a')]//2)
            else:
                ans = min(ans, hash[ord(i) - ord('a')])
        return ans 