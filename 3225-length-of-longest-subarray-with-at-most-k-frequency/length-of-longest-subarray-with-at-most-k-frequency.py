class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        dic = defaultdict(int)
        l=0
        for r in range(n):
            dic[nums[r]] += 1
            while dic[nums[r]] > k:
                dic[nums[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans