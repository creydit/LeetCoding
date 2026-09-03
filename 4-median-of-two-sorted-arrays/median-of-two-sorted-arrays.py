class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        i = 0
        j = 0 
        target = n//2
        prev = -1
        curr = -1
        while target>=0:
            target -= 1
            prev = curr
            if i < n1 and (j >= n2 or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
        if n%2==0:
            return (curr+prev)/2
        return curr