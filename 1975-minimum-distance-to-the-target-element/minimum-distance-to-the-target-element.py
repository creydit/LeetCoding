class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        ans = 1e9
        for i in range(n):
            if nums[i] == target:
                ans = min(ans, abs(i-start))
        '''
        for i in range(start):
            if nums[i] == target:
                ans = min(ans, abs(i-start))
        for i in range(start, n):
            if nums[i] == target:
                ans = min(ans, abs(i-start))
        '''
        return ans 