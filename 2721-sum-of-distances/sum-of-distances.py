class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = defaultdict(list)
        for i in range(n):
            dic[nums[i]].append(i)
        
        ans = [0]*n
        for num,idx in dic.items():
            n1 = len(idx)
            if n1==1:
                continue
            p = [0]*n1
            p[0] = idx[0]
            for i in range(1,n1):
                p[i] = idx[i]+p[i-1]

            for i in range(n1):
                if i==0:
                    ans[idx[i]] = p[-1] - n1*idx[i]
                    continue
                l = abs(i*idx[i] - p[i-1])
                r = abs((p[-1] - p[i]) - (n1-i-1)*idx[i])
                ans[idx[i]] = (l+r)
        return ans
                


            