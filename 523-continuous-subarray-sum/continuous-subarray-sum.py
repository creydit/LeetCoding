class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        n = len(nums)

        pref = [0]*(n+1)
        for i in range(n):
            pref[i+1] = pref[i] + nums[i]

        dic = {}
        
        for i in range(n+1):
            r = pref[i] % k
            x = dic.get(r, -1)
            if x == -1:
                dic[r] = i
                continue
            if i - x >= 2:
                return True 
        return False
                