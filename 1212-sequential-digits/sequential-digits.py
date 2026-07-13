class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:\
        #Using BFS
        q = [i for i in range(1,10)]
        for i in q:
            d = i%10
            if d < 9:
                q.append(i*10 + d + 1)
        ans = []
        for i in q:
            if low<=i<=high:
                ans.append(i)
        return ans
        
        #TC - O(nlogn, n is max num of increasing digits) and SC - O(1)
        '''
        ans = []
        s = '123456789'
        l = 0
        for l in range(9):
            numS = ''
            for r in range(l,9):
                numS+=s[r]
                num = int(numS)
                if low<=num<=high:
                    ans.append(num)
        ans.sort()
        return ans
        '''
