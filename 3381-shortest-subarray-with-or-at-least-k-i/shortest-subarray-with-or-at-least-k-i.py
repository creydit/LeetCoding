class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 10**18
        found = False
        for i in range(n):
            aur = nums[i]
            for j in range(i,n):
                aur = aur | nums[j]
                if aur >= k:
                    found = True
                    ans = min(ans, j-i+1)
        if found:
            return ans
        return -1