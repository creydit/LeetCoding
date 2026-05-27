class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        dic = defaultdict(int)
        dic1 = defaultdict(int)
        for i in word:
            dic[i] += 1
    
        for i in word:
            dic1[i] += 1
            if i.isupper():
                x = i.lower()
                if dic1[x] == dic[x] and dic[x] > 0 and dic1[i] == 1:
                    ans += 1
                    dic[x] -= 1
        return ans