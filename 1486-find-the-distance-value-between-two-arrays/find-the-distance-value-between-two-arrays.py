class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
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