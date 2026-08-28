class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        ans = 0
        coverStart = intervals[0][0]
        coverEnd = intervals[0][1]
        for i in range(1,n):
            currS = intervals[i][0]
            currE = intervals[i][1]
            if coverEnd <= currS:
                coverStart = currS
                coverEnd = currE
            elif currE <= coverEnd:
                ans += 1
                coverStart = currS
                coverEnd = currE
            elif currS <= coverEnd:
                ans += 1
        return ans 