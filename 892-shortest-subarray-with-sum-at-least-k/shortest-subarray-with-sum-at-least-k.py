class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        #Real Optimal 
        #TC - O(n) and SC - O(n)
        n = len(nums)
        q = deque()
        pref = [0]
        for i in range(n):
            pref.append(pref[-1] + nums[i])
        ans = 10**18
        for i in range(n+1):
            while q and pref[i] - pref[q[0]] >= k:
                idx = q.popleft()
                ans = min(ans, i - idx)
            while q and pref[i] <= pref[q[-1]]:
                q.pop()
            q.append(i)
        if ans==10**18:
            return -1
        return ans



        #Optimal by sliding window
        #not optimal as it cannot account for negatives
        '''
        n = len(nums)
        l = 0
        ss = 0
        ans = 10**18
        for r in range(n):
            ss += nums[r] 
            while ss >= k:
                ans = min(ans, r - l + 1)
                ss -= nums[l]
                l += 1
        l = n-1
        ss=0
        for r in range(n-1,-1,-1):
            ss += nums[r] 
            while ss >= k:
                ans = min(ans, l - r + 1)
                ss -= nums[l]
                l -= 1
        if ans==10**18:
            return -1
        return ans 
        '''
        #Brute force appproach 
        #TC - O(n^2) and SC - O(1)
        '''
        n = len(nums)
        ans = 10**18
        for i in range(n):
            ss = 0
            for j in range(i,n):
                ss += nums[j]
                if ss >= k:
                    ans = min(ans,j-i+1)
        if ans==10**18:
            return -1
        return ans 
        '''