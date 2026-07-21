class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
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