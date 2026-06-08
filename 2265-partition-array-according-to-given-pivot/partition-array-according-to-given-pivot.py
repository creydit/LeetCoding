class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        #Brute force
        n = len(nums)
        smalls = []
        equals = []
        bigs = []
        for i in nums:
            if i < pivot:
                smalls.append(i)
            elif i == pivot:
                equals.append(i)
            else:
                bigs.append(i)
        ans = smalls+equals+bigs
        return ans 