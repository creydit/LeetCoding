class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for i in s:
            if i.isalpha():
                ans += i
            elif i == '*' and len(ans)>=1:
                ans = ans[:-1]
            elif i == '#':
                ans += ans
            elif i == '%':
                ans = ans[::-1]
        return ans