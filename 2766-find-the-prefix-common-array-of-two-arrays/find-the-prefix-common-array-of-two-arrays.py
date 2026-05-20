class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        hash = [0]*(n+1)
        ans = [0]*n
        common = 0
        for i in range(n):
            hash[A[i]] += 1
            if hash[A[i]] >= 2:
                common += 1
            hash[B[i]] += 1
            if hash[B[i]] >= 2:
                common += 1
            ans[i] = common
        return ans
            
            