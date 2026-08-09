class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = defaultdict(int)
        for i in tasks:
            dic[i] += 1
        mx = -10**18
        vals = 1
        for char, v in dic.items():
            if v > mx:
                mx = v
                vals=1
            elif v==mx:
                vals+=1
        ans = max(len(tasks), (mx-1)*(n+1) + vals)
        return ans 

