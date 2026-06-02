class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        #optimal by finding best possible activity (least timer) to finish first and then doing the second best
        def solve(s1, d1, s2,d2):
            n = len(s1)
            m = len(s2)
            f1 = 10**18
            for i in range(n):
                f1 = min(f1, s1[i] + d1[i])
            f2 = 10**18
            for i in range(m):
                f2 = min(f2, max(f1,s2[i]) + d2[i])
            return f2

        lw = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        wl = solve(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(lw,wl)
        
        
        
        #Brute Force
        '''
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
        '''
                
