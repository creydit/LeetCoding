class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # optimal by sliding window, check c++ for more info.
        # TC - O(n) and SC - O(2)
        n = len(fruits)
        dic = {}
        ans = 0
        l = 0
        r = 0
        while r < n:
            if fruits[r] not in dic:
                dic[fruits[r]] = 1
            else:
                dic[fruits[r]] += 1
            if (len(dic) > 2):
                dic[fruits[l]] -= 1
                if(dic[fruits[l]] == 0): del dic[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans