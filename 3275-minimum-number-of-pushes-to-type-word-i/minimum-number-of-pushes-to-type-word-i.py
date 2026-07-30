class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) <= 8:
            return len(word)
        ans = 0
        num = 1
        x = 1
        for i in word:
            if num==9:
                num = 1
                x += 1
            ans += x
            num += 1
        return ans