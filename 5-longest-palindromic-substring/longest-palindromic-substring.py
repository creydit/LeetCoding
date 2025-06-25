class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        #Optimal solution without DP 
        #using 2 pointer to go out from a mid of palindrome 
        # TC-O(n2) and SC-O(n) for storing ans 
        # can be improved by DP but for now I'm doing strings
        ans=''
        ansl=0
        for i in range(n):
            #odd lengths
            l,r=i,i
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>ansl:
                    ans=s[l:r+1]
                    ansl=(r-l+1)
                l-=1
                r+=1
            #even length
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>ansl:
                    ans=s[l:r+1]
                    ansl=(r-l+1)
                l-=1
                r+=1
        return ans

        # Brute force approach involve checking every substring that is it a palindrome 
        # finding every substring = O(n2) and then checking is is a palindrome O(n)
        # TC - O(n3) and SC-O(n)
        '''
        ans=""
        for i in range(n):
            for j in range(i,n):
                x=s[i:j]
                if is_palindrome(x) and len(x)>len(ans): 
                    ans=x
        return ans
        '''
                    
