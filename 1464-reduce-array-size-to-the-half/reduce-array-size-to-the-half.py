class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        half = n//2
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse = True))
        ans = 0
        ss = 0
        for i,j in dic.items():
            ss += j
            ans += 1
            if ss >= half:
                break
        return ans