class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        m = 1
        x = n
        while x:
            d = x%10
            x //= 10
            if d!=0:
                ans.append(m*d)
            m *= 10
        ans = ans[::-1]
        return ans 