class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hash = set()
        for i in arr1:
            while i not in hash and i > 0:
                hash.add(i)
                i//=10
        
        ans = 0
        for i in arr2:
            while i not in hash and i > 0:
                i//=10
            if i>0:
                ans = max(ans, len(str(i)))
        
        return ans 