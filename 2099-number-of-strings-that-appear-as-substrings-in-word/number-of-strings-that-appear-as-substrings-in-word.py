class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        #Brute force approach
        #TC - O(len(patterns) * len(word)) and SC - O(1)
        ans = 0
        for i in patterns:
            if i in word:
                ans += 1
        return ans 