class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        def ds(n):
            ss = 0
            while n > 0:
                ss += n%10
                n//=10
            return ss

        arr = [0]*n
        for i in range(n):
            arr[i] = ds(nums[i])
        
        return min(arr)