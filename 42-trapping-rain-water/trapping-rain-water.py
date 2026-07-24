class Solution:
    def trap(self, height: List[int]) -> int:
        #using preffix max and suffix max 
        #TC - O(N+N+N) and SC- O(N+N)
        n = len(height)
        prefmax = [0]*n
        prefmax[0] = height[0]
        suffmax = [0]*n
        suffmax[-1] = height[-1]
        for i in range(1,n):
            prefmax[i] = max(prefmax[i-1],height[i])
        for i in range(n-2,-1,-1):
            suffmax[i] = max(height[i], suffmax[i+1])
        ans = 0
        for i in range(n):
            if height[i] < prefmax[i] and height[i] < suffmax[i]:
                ans += min(prefmax[i],suffmax[i]) - height[i]
        return ans 