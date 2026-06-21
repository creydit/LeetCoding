class Solution:
    def maxDistance(self, moves: str) -> int:
        n = len(moves)
        nL = nR = nU = nD = nx = 0
        for i in moves:
            if i == 'L':
                nL += 1
            elif i == 'R':
                nR += 1
            elif i == 'U':
                nU += 1
            elif i == 'D':
                nD += 1
            else:
                nx += 1
        ans = abs(nL - nR) + abs(nU - nD)
        ans += nx
        return ans
