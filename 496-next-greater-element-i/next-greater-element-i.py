class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Optimal using monotonic stack and hahsmap
        #TC - O(n1 + n2) and SC - O(1)
        n1 = len(nums1)
        n2 = len(nums2)
        hashnums2 = [-1]*(10001)
        st = []
        for i in range(n2-1,-1,-1):
            while st and st[-1] < nums2[i]:
                st.pop()
            if st:
                hashnums2[nums2[i]] = st[-1]
            st.append(nums2[i])

        ans = [-1]*n1
        for i in range(n1):
            ans[i] = hashnums2[nums1[i]]
        return ans 

        #better 
        #TC - O(n^2) and SC- O(1)
        '''
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        for i in range(n1):
            ng = -1
            for j in range(n2-1,-1,-1):
                if nums2[j] > nums1[i]:
                    ng = nums2[j]
                elif nums2[j] == nums1[i]:
                    break
            ans.append(ng)
        return ans
        '''
        #Brute force
        #TC - O(n^3) and SC - O(1)
        '''
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
        '''