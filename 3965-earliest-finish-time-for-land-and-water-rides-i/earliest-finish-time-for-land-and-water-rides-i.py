class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        #Brute Force
        n = len(landStartTime)
        m = len(waterStartTime)
        ans = 10**18
        for i in range(n):
            for j in range(m):
                lride = landStartTime[i] + landDuration[i]
                lw = max(lride, waterStartTime[j]) + waterDuration[j]
                ans = min(ans, lw)

                wride = waterStartTime[j] + waterDuration[j]
                wl = max(wride, landStartTime[i]) + landDuration[i]
                ans = min(ans, wl)
        return ans 
                
