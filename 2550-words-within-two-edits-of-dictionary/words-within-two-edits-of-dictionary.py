class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        #Brute Force
        ans = []
        for word in queries:
            for d in dictionary:
                dis = 0
                for i in range(len(word)):
                    if word[i] != d[i]:
                        dis += 1
                if dis <= 2:
                    ans.append(word)
                    break
        return ans 