class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        n = len(nums)
        g = nums[0]
        for i in range(n):
            g = math.gcd(g, nums[i])
            if g==1:
                return True
        return False