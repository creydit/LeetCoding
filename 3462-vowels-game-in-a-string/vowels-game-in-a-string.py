class Solution:
    def doesAliceWin(self, s: str) -> bool:
        cnt = 0
        vowels = ['a','e','i','o','u']
        for i in s:
            if i in vowels:
                cnt += 1
        if cnt==0:
            return False
        return True