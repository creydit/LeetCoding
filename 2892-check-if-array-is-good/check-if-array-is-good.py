class Solution:
    def isGood(self, nums: List[int]) -> bool:
        #by sorting
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            if nums[i] != i+1:
                return False
        return nums[n-1] == n-1

        #by Me
        '''
        n = len(nums)
        mx = max(nums)
        base = [i for i in range(1,mx+1)]
        base.append(mx)
        if sorted(nums)!=base:
            return False
        return True
        '''