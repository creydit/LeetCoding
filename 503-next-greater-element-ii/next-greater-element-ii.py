class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #Optimal
        #TC - O(2N) and SC - O(2N)
        mynums = nums+nums
        n = len(nums)
        ans = []
        st = []
        for i in range(2*n - 1,-1,-1):
            while st and st[-1] <= mynums[i]:
                st.pop()
            
            if not st:
                ans.append(-1)
            else:
                ans.append(st[-1])
            st.append(mynums[i])
        ans = ans[::-1]
        ans = ans[:n]
        return ans 