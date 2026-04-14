class Solution:
    def maxRepOpt1(self, text: str) -> int:
        #TC - O(26 * n) ~ O(n) 
        #SC - O(26)
        n = len(text)
        dic = Counter(text)
        ans = 0
        for c in dic:
            left = 0
            mismatch = 0
            for right in range(n):
                if text[right] != c:
                    mismatch += 1
                while mismatch > 1:
                    if text[left] != c:
                        mismatch -=1
                    left += 1
                ans = max(ans , min(right - left + 1, dic[c]))
        return ans 

        

