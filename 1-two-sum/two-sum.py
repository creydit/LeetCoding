class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = defaultdict(int)
        for i in range(n):
            r = target - nums[i]
            if r in dic:
                return [i,dic[r]]
            dic[nums[i]] = i
        return [0,0]