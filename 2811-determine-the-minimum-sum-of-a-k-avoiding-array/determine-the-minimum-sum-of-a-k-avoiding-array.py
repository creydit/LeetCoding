class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        arr = []
        i = 1
        avoid = set()
        while len(arr) < n:
            if i in avoid:
                i += 1
                continue
            arr.append(i)
            avoid.add(k-i)
            i += 1
        return sum(arr)
