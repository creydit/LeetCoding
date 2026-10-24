class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        n = len(machines)
        ss = sum(machines)
        if ss % n != 0:
            return -1
        avg = ss // n
        leftsum = [0]*(n+1)
        rightsum = [0]*(n+1)
        for i in range(1,n):
            leftsum[i] = leftsum[i-1] + machines[i-1]
        for i in range(n-2,-1,-1):
            rightsum[i] = rightsum[i+1] + machines[i+1]
        ans = 0
        for i in range(n):
            expleft = i*avg
            expright = (n-i-1)*avg
            left = 0
            right = 0
            if expleft > leftsum[i]:
                left = expleft - leftsum[i]
            if expright > rightsum[i]:
                right = expright - rightsum[i]
            ans = max(ans, left+right)
        return ans