class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        #TC - O(1)
        return n

        
        #TC - O(logN)
        '''
        so = n*n
        se = n*(n+1)
        return math.gcd(so,se)
        '''

        #TC - O(N)
        '''
        numo = 1
        nume = 2
        so = 1
        se = 2
        for i in range(n-1):
            numo += 2
            nume += 2
            so += numo
            se += nume
        return math.gcd(so,se)
        '''