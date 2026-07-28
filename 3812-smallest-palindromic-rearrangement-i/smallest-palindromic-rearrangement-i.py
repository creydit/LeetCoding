class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        mp = defaultdict(int)
        for i in s:
            mp[i] += 1
        ans = ''
        ss = ''
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if mp[i] == 0:
                continue
            if mp[i] == 1:
                ss = i
                continue
            if mp[i]%2==1:
                ss = i
                ans += i*(mp[i]//2)
                continue
            ans += i*(mp[i]//2)
        temp = ans[::-1]
        ans += ss
        ans += temp
        return ans