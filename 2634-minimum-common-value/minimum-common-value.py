class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        #Optimal
        #TC - O(n^2)
        n1 = len(nums1)
        n2 = len(nums2) 
        i = 0
        j = 0
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
        #Better
        #TC - O(n^2 ) in worst cases
        '''
        n1 = len(nums1)
        n2 = len(nums2)
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    return nums1[i]
        '''

        #Brute 
        #TC - O(n2)
        '''
        n1 = len(nums1)
        n2 = len(nums2)
        ans = 10**18
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    ans = min(ans, nums1[i])
        return ans
        '''