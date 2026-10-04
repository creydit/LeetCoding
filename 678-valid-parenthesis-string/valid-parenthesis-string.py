class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        star = [] 
        st = []
        for i in range(n):
            if s[i] == '*':
                star.append(i)
            elif s[i] == '(':
                st.append(i)
            else:
                if st:
                    st.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while st and star:
            if st[-1] > star[-1]:
                return False
            st.pop()
            star.pop()
        return len(st) == 0