class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        inf = 10**20
        n = len(nums)
        prefMax = [0]*(n+1)
        suffMin = [inf]*(n+1)
        prefDrops = [0]*(n)

        for i in range(n):
            prefMax[i+1] = max(prefMax[i],nums[i])

        for i in range(n-1,-1,-1):
            suffMin[i] = min(suffMin[i+1],nums[i])
            
        for i in range(1,n):
            prefDrops[i] = prefDrops[i-1]
            if nums[i-1] > nums[i]:
                prefDrops[i] += 1

        def check(k):
            for start in range(0,n,k):
                end = start + k -1
                drops = prefDrops[end] - prefDrops[start]
                if nums[end] > nums[start]:
                    drops += 1
                if drops > 1:
                    return False
                if prefMax[start] > suffMin[start]:
                    return False
            return True
        
        ans = 0
        for i in range(1,n+1):
            if n%i==0 and check(i):
                ans += i
        return ans