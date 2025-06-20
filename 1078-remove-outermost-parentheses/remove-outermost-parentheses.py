class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened=0
        ans=""
        for i in s:
            if i=="(":
                if opened>0:
                    ans+=i
                opened+=1
            else:
                opened-=1
                if opened>0:
                    ans+=i
        return ans 

                    