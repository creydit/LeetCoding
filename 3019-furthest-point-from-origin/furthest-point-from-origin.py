class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count('L')
        r = moves.count('R')
        d = moves.count('_')
        return max(l,r)-min(l,r)+d