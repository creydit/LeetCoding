class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        newn = ''
        ss = 0
        while n:
            x = n%10
            ss += x
            if x!=0:
                newn += str(x)
            n//=10
        newn = int(newn[::-1])
        return ss*newn