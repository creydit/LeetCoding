class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        #Better Solution by reducing the inner 3rd loop as the 2nd loop will most of that job
        # TC- O(n2) and SC-O(1) as atmost 26 elements in dic
        ans=0
        for i in range(n):
            dic={}
            for j in range(i,n):
                if s[j] in dic:
                    dic[s[j]]+=1
                else:
                    dic[s[j]]=1
                maxi=max(dic.values())
                mini=min(dic.values())
                ans+=(maxi-mini)
        return ans

        # Brute force using 2 loops and counting all the substring and then finding the beauty
        # TC-O(n3) and SC-O(1) as dic atmost will have 26 letters
        '''
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                dic={}
                for k in range(i,j+1):
                    if s[k] in dic:
                        dic[s[k]]+=1
                    else:
                        dic[s[k]]=1
                maxi=max(dic.values())
                mini=min(dic.values())
                ans+=(maxi-mini)
        return ans
        ''' 
