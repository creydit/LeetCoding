class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
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