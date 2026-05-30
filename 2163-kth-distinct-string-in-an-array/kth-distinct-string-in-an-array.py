class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1
        for i in arr:
            if dic[i] == 1:
                k -= 1
            if k==0:
                return i
        return ""
