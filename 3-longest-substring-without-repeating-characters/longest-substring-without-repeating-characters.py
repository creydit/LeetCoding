class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # See C++ for explaination
        n = len(s)
        l = 0
        r = 0
        ans = 0
        hash = [-1] * 256
        while r < n:
            idx = ord('a') - ord(s[r])
            if hash[idx] != -1 and hash[idx] >= l:
                l = hash[idx] + 1
            hash[idx] = r
            ans = max(ans, r - l + 1)
            r+=1
        return ans 