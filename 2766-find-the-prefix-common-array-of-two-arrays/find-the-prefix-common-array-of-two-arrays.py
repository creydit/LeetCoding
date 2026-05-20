class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        hashA = [0]*(n+1)
        hashB = [0]*(n+1)
        ans = [0]*n
        common = 0
        for i in range(n):
            hashA[A[i]] = 1
            if hashB[A[i]] == 1:
                common += 1
            hashB[B[i]] = 1
            if hashA[B[i]] == 1:
                common += 1
            ans[i] = common
        return ans
            
            