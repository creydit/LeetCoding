class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        #TC - O(N) and SC - O(1)
        n = len(s)
        cnt1 = s.count('1')
        i = 0
        prev = -inf
        ans = 0
        while i < n:
            j = i
            while i < n and s[j]==s[i]:
                i+=1
            if s[j]=='0':
                curr = i-j
                ans = max(ans,prev+curr)
                prev = curr
        ans += cnt1
        return ans

        #TC - O(N) and SC -O(N)
        '''
        n = len(s)
        cnt1 = s.count('1')
        arr = []
        z = 0
        for i in range(n):
            if s[i]=='0':
                z+=1
            else:
                if z!=0:
                    arr.append(z)
                    z = 0
        if z!=0:
            arr.append(z)
        ans = 0
        for i in range(len(arr)-1):
            ans = max(ans, arr[i]+arr[i+1])
        ans += cnt1
        return ans
        '''