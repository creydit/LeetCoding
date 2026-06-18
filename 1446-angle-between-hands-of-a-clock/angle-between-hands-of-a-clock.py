class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mm = minutes*6.0
        hh = 30.0*(hour%12) + (0.5*minutes)
        ans = abs(hh-mm)
        return min(ans, 360.0-ans)