class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefgcd = [0]*n
        mx = -1
        for i in range(n):
            mx = max(mx,nums[i])
            prefgcd[i] = math.gcd(nums[i],mx)
        prefgcd.sort()
        ans = 0
        for i in range(n//2):
            ans += math.gcd(prefgcd[i],prefgcd[n-1-i])
        return ans
        