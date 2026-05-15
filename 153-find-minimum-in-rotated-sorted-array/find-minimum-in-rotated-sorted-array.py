class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo = 0
        hi = n-1
        mini = 10**18
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[lo] <= nums[hi]:
                mini = min(mini, nums[lo])
                break
            if nums[lo] <= nums[mid]:
                mini = min(mini, nums[lo])
                lo = mid + 1
            else:
                mini = min(mini, nums[mid])
                hi = mid - 1
        return mini