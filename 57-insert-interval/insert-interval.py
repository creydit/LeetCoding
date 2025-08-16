class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals):
            n = len(intervals)
            intervals.sort()
            ans = []
            ans.append(intervals[0])
            for i in range(1,n):
                s1 = ans[-1][0]
                e1 = ans[-1][1]
                s2 = intervals[i][0]
                e2 = intervals[i][1]
                if s2 <= e1:
                    ans.pop()
                    x = min(s1,s2)
                    y = max(e1,e2)
                    ans.append([x,y])
                else:
                    ans.append([s2,e2])
            return ans

        intervals.append(newInterval)
        return merge(intervals)

