class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mi = min(nums)
        return math.gcd(mx,mi)