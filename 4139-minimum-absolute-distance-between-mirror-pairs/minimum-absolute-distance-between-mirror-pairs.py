class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(int)
        ans = inf
        for i in range(n):
            x = int(str(nums[i])[::-1])
            if nums[i] in dic:
                ans = min(ans, i - dic[nums[i]])
            dic[x] = i

        return ans if ans!=inf else -1
        '''
        #Pure Mine 
        n = len(nums)

        arr = []
        for i in range(n):
            arr.append((nums[i],i))

        arr.sort()

        def rev(n):
            s = str(n)
            s = s[::-1]
            for i in range(len(s)):
                if s[i]=='0':
                    continue
                else:
                    break
            return int(s[i:])
        ans = 1000000000
        ok = False
        for i in range(n):
            num = arr[i][0]
            x = rev(num)
            lo = 0
            hi = n-1
            while lo <= hi:
                mid = (lo+hi)//2
                if arr[mid][0] <= x:
                    if arr[mid][0] == x and arr[mid][1] > arr[i][1]:
                        ok = True
                        ans = min(ans,abs(arr[mid][1] - arr[i][1]))
                    lo = mid + 1
                elif arr[mid][0] > x:
                    hi = mid - 1
        if not ok:
            return -1
        return ans
        '''
