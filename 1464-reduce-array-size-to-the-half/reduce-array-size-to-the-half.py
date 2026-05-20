class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        half = n//2
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1
        freq = sorted(dic.values(),reverse = True)
        ans = 0
        ss = 0
        for i in freq:
            ss += i
            ans += 1
            if ss >= half:
                break
        return ans