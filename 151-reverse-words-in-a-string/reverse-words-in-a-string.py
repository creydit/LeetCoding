class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        ans=""
        for i in range(len(l)-1,-1,-1):
            if l[i]=="":
                l.remove(l[i])
        for i in range(len(l)-1,-1,-1):
            if l[i]!="":
                ans+=l[i]
                if i!=0:
                    ans+=" "
        return ans 
        