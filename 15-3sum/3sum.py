class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            val1 = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                val2 = nums[j]
                val3 = nums[k]
                ss = val1+val2+val3
                if ss == 0:
                    ans.append((val1, val2, val3))
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif ss < 0:
                    j += 1
                else:
                    k -= 1
        return ans
        
        