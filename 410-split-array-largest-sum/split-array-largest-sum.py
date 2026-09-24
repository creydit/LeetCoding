class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        lo = max(nums)
        hi = 10**9
        while lo <= hi:
            mid = (lo+hi)//2
            s = 0
            cnt = 0
            for i in range(n):
                if s+nums[i]<=mid:
                    s += nums[i]
                else:
                    s = nums[i]
                    cnt += 1
            if s > 0:
                cnt += 1
            if cnt > k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo