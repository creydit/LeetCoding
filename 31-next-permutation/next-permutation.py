class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = -1
        for i in range(n-2,-1,-1):
            if nums[i+1] > nums[i]:
                idx = i
                break
        if idx == -1:
           nums.reverse()
        else:
            for i in range(n-1,-1,-1):
                if nums[i] > nums[idx]:
                    nums[i],nums[idx] = nums[idx],nums[i]
                    break
            i = idx+1
            j = n-1
            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1

            