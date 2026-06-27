class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in nums1:
            if i in nums2:
                return i
        no1 = nums1[0]*10 + nums2[0]
        no2 = nums2[0]*10 + nums1[0]
        ans = min(no1,no2)
        return ans