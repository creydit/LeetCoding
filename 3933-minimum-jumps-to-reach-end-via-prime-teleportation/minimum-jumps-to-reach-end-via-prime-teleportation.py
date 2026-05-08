mx = 1000001
fac = defaultdict(list)
for i in range(2,mx):
    if not fac[i]:
        for j in range(i,mx,i):
            fac[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        edges = defaultdict(list)
        for i, a in enumerate(nums):
            for p in fac[a]:
                edges[p].append(i)
        res = 0
        seen = [False] * n
        seen[0] = True
        q = [0]
        while True:
            q2 = []
            for i in q:
                if i == n - 1:
                    return res
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                if len(fac[nums[i]]) == 1:
                    p = nums[i]
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    edges[p].clear()
            q = q2
            res += 1
        return res










        '''
        def isp(n):
            x = 2
            while x <= math.sqrt(n):
                if n%x==0:
                    return False
                x += 1
            return True
        
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == 1:
                ans += 1
                continue
            if isp(nums[i]) and nums[-1]%nums[i]==0:
                ans += 1
                break
            else:
                ans += 1
        if ans==n:
            ans -= 1
        return ans
        '''