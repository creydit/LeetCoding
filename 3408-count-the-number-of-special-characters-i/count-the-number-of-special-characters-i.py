class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        dic = defaultdict(int)
        for i in word:
            dic[i] += 1
        ans = 0
        for i in word:
            if i.islower():
                if dic[i.upper()] > 0:
                    dic[i.upper()] = 0
                    ans += 1
        return ans