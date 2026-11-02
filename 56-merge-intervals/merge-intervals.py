class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)
        intervals.sort()
        ans = []
        ans.append(intervals[0])
        for i in range(1,n):
            curr = ans.pop()
            currS = curr[0]
            currE = curr[1]
            atS = intervals[i][0]
            atE = intervals[i][1]
            if currE < atS:
                ans.append(curr)
                ans.append(intervals[i])
            else:
                s = min(currS, atS)
                e = max(currE, atE)
                ans.append([s,e])
        return ans

        #    ---------
        # -----    -------
        #      ---- 
        # 2 3  5  6 7 8  10