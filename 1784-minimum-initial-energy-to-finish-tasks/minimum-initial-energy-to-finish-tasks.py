class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        n = len(tasks)
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)
        ans = 0
        curr = 0
        for i in range(n):
            if i==0:
                ans = tasks[i][1]
                curr = tasks[i][1]
                curr -= tasks[i][0]
                continue
            if curr >= tasks[i][1]:
                curr -= tasks[i][0]
            else:
                needed = tasks[i][1] - curr
                ans += needed
                curr = tasks[i][1]
                curr -= tasks[i][0]
        return ans
        