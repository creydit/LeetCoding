class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        evens = []
        odds = []
        for i in range(n):
            if nums[i]%2==0:
                evens.append(i)
            else:
                odds.append(i)
                
        if abs(len(evens) - len(odds)) > 1:
            return -1

        def solve(idx):
            swaps = 0
            for i in range(len(idx)):
                swaps += abs(idx[i] - 2*i)
            return swaps

        ans = float('inf')
        if len(evens) >= len(odds):
            ans = solve(evens)
        if len(odds) >= len(evens):
            ans = min(ans, solve(odds))
        return ans 