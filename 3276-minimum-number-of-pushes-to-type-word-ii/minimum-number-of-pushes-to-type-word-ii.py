class Solution:
    def minimumPushes(self, word: str) -> int:
        dic = [0]*26
        for i in word:
            dic[ord(i) - ord('a')] += 1
        dic.sort(reverse = True)
        ans = 0
        for i in range(26):
            if dic[i]==0:
                break
            ans += (i//8 + 1)*dic[i]
        return ans