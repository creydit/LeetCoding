class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            curr = max(nums[i], nums[i] + curr)
            ans = max(ans, curr)
        return ans        