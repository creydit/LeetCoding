class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #TC - O(nlogn) and SC - O(1)
        intervals.sort(key = lambda x: (x[0],-x[1]))
        ans = 0
        maxend = -1
        for s,e in intervals:
            if maxend < e:
                ans += 1
                maxend = e
        return ans


        #TC - O(nlogn) and SC - O(n)
        '''
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0],-x[1]))
        ans = [intervals[0]]
        for i in range(1,n):
            lasts = ans[-1][0]
            laste = ans[-1][1]
            currs = intervals[i][0]
            curre = intervals[i][1]
            if lasts <= currs and curre <= laste:
                continue
            else:
                ans.append(intervals[i])
        return len(ans)
        '''
