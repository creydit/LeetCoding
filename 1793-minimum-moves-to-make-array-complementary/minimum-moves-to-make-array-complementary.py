class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0]*(2*limit + 2)
        for i in range(n//2):
            x = nums[i]
            y = nums[n-i-1]
            a = min(x,y)
            b = max(x,y)
            diff[2] += 2
            diff[a+1] -= 1
            diff[a+b] -= 1
            diff[a+b+1] += 1
            diff[b+limit+1] += 1
        ans = n
        curr = 0
        for i in range(2,2*limit + 1):
            curr += diff[i]
            ans = min(ans, curr)
        return ans
            