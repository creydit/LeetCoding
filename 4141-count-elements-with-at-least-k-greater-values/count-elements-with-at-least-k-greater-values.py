class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        #Optimal 
        #TC - O(nlogn)
        ans = 0
        n = len(nums)
        nums.sort(reverse = True)
        i = 0
        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
                
            if i >= k:
                ans += j-i
            i = j
        return ans 

        #Brute force
        #TC - O(n^2)
        '''
        n = len(nums)
        ans = 0
        for i in range(n):
            g = 0
            for j in range(n):
                if nums[i] > nums[j]:
                    g += 1
            if g >= k:
                ans += 1
        return ans 
        '''