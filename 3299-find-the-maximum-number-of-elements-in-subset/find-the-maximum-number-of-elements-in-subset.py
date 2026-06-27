class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dic = Counter(nums)
        one = dic.get(1,0)
        if one%2==1:
            ans = one
        else:
            ans = one-1
        dic.pop(1,None)
        for i in dic:
            res = 0
            x = i
            while x in dic and dic[x] > 1:
                res += 2
                x*=x
            ans = max(ans, res + (1 if x in dic else -1))
        return ans 