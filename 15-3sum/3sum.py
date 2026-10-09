class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            val1 = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                val2 = nums[j]
                val3 = nums[k]
                ss = val1+val2+val3
                if ss == 0:
                    ans.add((val1, val2, val3))
                    j += 1
                    k -= 1
                elif ss < 0:
                    j += 1
                else:
                    k -= 1
        ans2 = []
        for i in ans:
            ans2.append(i)
        return ans2
        
        