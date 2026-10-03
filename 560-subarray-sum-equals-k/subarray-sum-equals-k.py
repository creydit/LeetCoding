class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        ss = 0
        dic = defaultdict(int)
        dic[0] = 1
        for i in range(n):
            ss += nums[i]
            if ss - k in dic:
                ans += dic[ss-k]
            dic[ss] += 1
        return ans