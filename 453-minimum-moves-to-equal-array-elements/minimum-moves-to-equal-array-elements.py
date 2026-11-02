class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        curr = nums[0]
        diff = 0
        for i in range(n-1,0,-1):
            x = nums[i] + ans
            diff = x - curr
            ans += diff
            curr += diff
        return ans
