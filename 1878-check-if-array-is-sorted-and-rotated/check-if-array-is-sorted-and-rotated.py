class Solution:
    def check(self, nums: List[int]) -> bool:
        most = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                most += 1
        return most <= 1