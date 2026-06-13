class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        #TC - O(len(words) * len(word[i])) SC - O(26)
        hashrev = "zyxwvutsrqponmlkjihgfedcba"
        ans = ''
        for word in words:
            ss = 0
            for i in word:
                ss += weights[ord(i) - ord('a')]
            idx = ss%26
            ans += hashrev[idx]
        return ans