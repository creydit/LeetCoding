class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        #Another 2 pointer approach
        n = len(nums)
        ans = [0]*n
        li = 0
        gi = n-1
        for i in range(n):
            if nums[i] < pivot:
                ans[li] = nums[i]
                li += 1
        for j in range(n-1,-1,-1):
            if nums[j] > pivot:
                ans[gi] = nums[j]
                gi -= 1
        while li <= gi:
            ans[li] = pivot
            li += 1
        return ans
        #TC - O(n) and SC - O(n)
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