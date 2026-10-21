class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        ss = ''.join(sorted(s))
        if ss == s:
            return 0
        if n==2:
            return -1
        if ss[0] == s[0] or ss[-1] == s[-1]:
            return 1
        if ss[0] in s[1:-1] or ss[-1] in s[1:-1]:
            return 2
        return 3