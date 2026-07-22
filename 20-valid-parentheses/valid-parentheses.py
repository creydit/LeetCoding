class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        dic = { '(':')', '[':']', '{':'}'}
        for i in s:
            if i=='(' or i=='[' or i=='{':
                st.append(i)
            else:
                if len(st)==0 or i != dic[st.pop()]:
                    return False
        return len(st)==0