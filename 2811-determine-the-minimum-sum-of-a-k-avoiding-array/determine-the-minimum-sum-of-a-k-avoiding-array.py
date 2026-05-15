class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ss = 0
        l = 0
        i = 1
        avoid = set()
        while l < n:
            if i in avoid:
                i += 1
                continue
            if i >= k:
                ss += i
                i += 1
                l += 1
                continue
            ss += i
            avoid.add(k-i)
            l += 1
            i += 1
        return ss
