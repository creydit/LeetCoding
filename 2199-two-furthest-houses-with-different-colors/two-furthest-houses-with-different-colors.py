class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = -int(1e9)
        for i in range(n):
            if colors[i] != colors[0]:
                ans = max(ans, i)
            if colors[i] != colors[-1]:
                ans = max(ans, n-1-i)
        return ans

        #Brute Force - O(n2)
        '''
        ans = -int(1e9)
        n = len(colors)
        for i in range(n):
            for j in range(i+1,n):
                if colors[i] != colors[j]:
                    ans = max(ans, j - i)
        return ans 
        '''