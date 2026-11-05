class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        n = len(arr1)
        m = len(arr2)
        ans = 0
        
        def bs(x):
            lo = 0
            hi = m-1
            while lo < hi:
                mid = (lo+hi)//2
                if arr2[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        for i in range(n):
            x = arr1[i]
            p = bs(x)
            if abs(x - arr2[p]) > d:
                if p == 0 or abs(x - arr2[p-1]) > d:
                    ans += 1
        return ans
        #TC - O(n2)
        '''
        n = len(arr1)
        m = len(arr2)
        ans = 0
        for i in range(n):
            ok = True
            for j in range(m):
                if abs(arr1[i] - arr2[j]) <= d:
                    ok = False
            if ok:
                ans += 1
        return ans
        '''