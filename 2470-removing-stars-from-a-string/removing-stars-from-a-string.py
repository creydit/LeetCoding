class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        st = []
        for i in range(n):
            if s[i] != '*':
                st.append(s[i])
            else:
                if st:
                    st.pop()
        ans=''
        while st:
            ans += st.pop()
        ans = ans[::-1]
        return ans