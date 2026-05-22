class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = n*2
        n3 = n*3
        s = str(n) + str(n2) + str(n3)
        hash = [0]*10
        for i in s:
            hash[int(i)] += 1
        ok = True
        for i in range(1,10):
            if hash[i] != 1:
                ok = False
                break
        return ok 