class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        st = []
        for i in range(n):
            x = num[i]
            while st and k > 0 and st[-1] > x:
                st.pop()
                k -= 1
            st.append(x)

        while k > 0:
            st.pop()
            k -= 1

        ans = ''
        zero = 1
        for i in st:
            if zero==0:
                ans += i
                continue
            if zero and i=='0':
                continue
            else:
                ans += i
                zero = 0
        return ans if ans else '0'
