class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        evenans = 0
        for i in range(0,n,2):
            if i==0 and n>1:
                if nums[0] >= nums[1]:
                    evenans += nums[0] - nums[1] + 1
                continue
            if i==n-1:
                if nums[i] >= nums[i-1]:
                    evenans += nums[i] - nums[i-1] + 1
                continue
            if nums[i] >= nums[i-1]:
                if nums[i] >= nums[i+1]:
                    evenans += nums[i] - min(nums[i-1], nums[i+1]) + 1
                    continue
                else:
                    evenans += nums[i] - nums[i-1] + 1
            else:
                if nums[i] >= nums[i+1]:
                    evenans += nums[i] - nums[i+1] + 1
        oddans = 0    
        for i in range(1,n,2):
            if i==n-1:
                if nums[i] >= nums[i-1]:
                    oddans += nums[i] - nums[i-1] + 1
                continue
            if nums[i] >= nums[i-1]:
                if nums[i] >= nums[i+1]:
                    oddans += nums[i] - min(nums[i-1], nums[i+1]) + 1
                    continue
                else:
                    oddans += nums[i] - nums[i-1] + 1
            else:
                if nums[i] >= nums[i+1]:
                    oddans += nums[i] - nums[i+1] + 1

        return min(evenans, oddans)
