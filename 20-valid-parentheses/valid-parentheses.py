class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic = { '(' : ')', '[' : ']', '{':'}'}
        for i in s:
            if i in ['(', '[', '{']:
                st.append(i)
            else:
                if not st or i != dic[st.pop()]:
                    return False
        return len(st) == 0