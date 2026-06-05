class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        maxi = max(milestones)
        ss = sum(milestones)
        x = ss - maxi
        if x >= maxi:
            return ss
        else:
            return 2*x + 1
