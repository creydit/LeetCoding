class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = [0]*32

        def getOR():
            curr = 0
            for i in range(32):
                if bits[i] > 0:
                    curr |= (1 << i)
            return curr

        l = 0
        ans = 10**18
        for r in range(n):
            for i in range(32):
                if nums[r] & (1 << i):
                    bits[i] += 1

            while l <= r and getOR() >= k:
                ans = min(ans, r - l + 1)
                for i in range(32):
                    if nums[l] & (1 << i):
                        bits[i] -= 1
                l += 1
        if ans==10**18:
            return -1
        return ans 