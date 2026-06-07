class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(idx):
            if idx == len(nums):
                ans.append(nums[:])
                return 
            for j in range(idx,len(nums)):
                nums[idx],nums[j] = nums[j],nums[idx]
                solve(idx+1)
                nums[idx],nums[j] = nums[j],nums[idx]
        solve(0)
        return ans 
            