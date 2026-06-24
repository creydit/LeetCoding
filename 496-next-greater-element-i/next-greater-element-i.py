class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        for i in range(n1):
            f = False
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    for k in range(j+1, n2):
                        if nums2[k] > nums2[j]:
                            f = True
                            ans.append(nums2[k])
                            break
            if not f:
                ans.append(-1)
        return ans 