from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        d = collections.Counter(nums)
        newd = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        ans = []
        for i, j in newd.items():
            if k>0:
                ans.append(i)
                k-=1
        return ans 

        