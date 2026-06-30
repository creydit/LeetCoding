class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        a=0
        b=0
        c=0
        l=0
        ans=0
        for r in range(n):
            if s[r]=='a':
                a+=1
            elif s[r]=='b':
                b+=1
            else:
                c+=1
            while a>0 and b>0 and c>0:
                ans+=n-r
                if s[l]=='a':
                    a-=1
                elif s[l]=='b':
                    b-=1
                else:
                    c-=1
                l += 1
        return ans 