class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        mpp = {}
        ans = 0
        l = 0
        for r in range(n):
            if fruits[r] not in mpp:
                mpp[fruits[r]]=1
            else:
                mpp[fruits[r]] += 1
            while len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]]==0:
                    del mpp[fruits[l]]
                l += 1
            ans = max(ans, r-l+1)
        return ans