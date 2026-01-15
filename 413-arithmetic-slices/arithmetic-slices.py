class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans= 0
        curr= 0
        for i in range(1,n-1):
            if nums[i-1] - nums[i] == nums[i] - nums[i+1]:
                curr+=1
                ans+=curr
            else:
                curr = 0
        return ans
                