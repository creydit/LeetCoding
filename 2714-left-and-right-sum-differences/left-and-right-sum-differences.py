class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Better Beats code
        totsum = sum(nums)
        left = 0 
        ans = []
        for i in nums:
            ans.append(abs(totsum - left - i))
            left += i
            totsum -= i
        return ans

        #Optimal 2 pass O(N) solution
        '''
        n = len(nums)
        ans = [0]*n
        runsum = 0
        totsum = sum(nums)
        for i in range(n):
            left = runsum
            runsum += nums[i]
            right = totsum - runsum
            ans[i] = abs(left - right)
        return ans
        '''