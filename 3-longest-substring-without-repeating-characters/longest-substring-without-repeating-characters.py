class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # See C++ for explaination
        n = len(s)
        l = 0
        ans = 0
        mpp = [0]*256
        for r in range(n):
            mpp[ord(s[r]) - ord('a')] += 1 
            while mpp[ord(s[r]) - ord('a')] > 1:
                mpp[ord(s[l]) - ord('a')] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans