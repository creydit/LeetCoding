class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        l = 0
        ans = 0
        slist = SortedList()
        for r in range(n):
            slist.add(nums[r])
            while slist[-1]-slist[0] > limit:
                slist.remove(nums[l])
                l += 1
            ans = max(ans, r-l+1)
        return ans