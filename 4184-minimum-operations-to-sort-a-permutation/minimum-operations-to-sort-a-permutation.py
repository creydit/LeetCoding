class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = -1

        for i in range(n):
            if nums[i] == 0:
                zero = i
                break

        def check(step):
            for i in range(1, n):
                curr = (zero + i*step)%n
                prev = (zero + (i-1)*step)%n
                if nums[prev] > nums[curr]:
                    return False
            return True
        
        ans = 10**18

        if check(1):
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)

        if check(-1):
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)

        if ans == 10**18:
            return -1

        return ans