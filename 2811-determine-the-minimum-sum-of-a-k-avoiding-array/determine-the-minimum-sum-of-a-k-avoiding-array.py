class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ss = 0
        l = 0
        i = 1
        check = [0]*10**5
        while l < n:
            if check[i]:
                i += 1
                continue
            if i >= k:
                ss += i
                i += 1
                l += 1
                continue
            ss += i
            check[k-i] = 1
            l += 1
            i += 1
        return ss
