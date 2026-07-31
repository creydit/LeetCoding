class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        ans = []
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                ans.append(nums[i])
        return ans