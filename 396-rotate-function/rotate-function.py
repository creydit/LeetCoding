class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        #Better 
        #TC - O(n)
        n = len(nums)
        ss = sum(nums)
        fi = 0
        for i in range(n):
            fi += i*nums[i]

        ans = fi

        for i in range(n-1,0,-1):
            fiplus1 = fi + ss - n*nums[i]
            ans = max(ans,fiplus1)
            fi = fiplus1

        return ans 


        '''
        #Brtue Force
        #TC - O(n^2)
        def solve(arr):
            ans = 0
            for i in range(len(arr)):
                ans += i*arr[i]
            return ans
        
        ans = -int(1e9)
        n = len(nums)
        for i in range(n):
            nums = [nums[-1]] + nums[:n-1]
            ans = max(ans, solve(nums))
        return ans 
        '''