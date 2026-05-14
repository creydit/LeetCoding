class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        mx = max(nums)
        base = [i for i in range(1,mx+1)]
        base.append(mx)
        if sorted(nums)!=base:
            return False
        return True