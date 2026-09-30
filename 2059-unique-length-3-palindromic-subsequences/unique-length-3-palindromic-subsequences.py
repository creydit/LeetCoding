class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #one more shorter one
        ans = 0
        for c in set(s):
            i = s.find(c)
            j = s.rfind(c)
            if j - i > 1:
                ans += len(set(s[i+1:j]))
        return ans

        
        #from 2848 - good approach
        '''
        n = len(s)
        right = [0]*26

        for i in range(n):
            right[ord(s[i]) - ord('a')] += 1

        left = [0]*26
        seen = set()
        for i in range(n):
            x = s[i]
            right[ord(x) - ord('a')] -= 1
            for c in range(26):
                if left[c] > 0  and right[c] > 0:
                    seen.add((c,x))
            left[ord(x)- ord('a')] += 1

        return len(seen)
        '''