class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        arr = nums.copy()
        mod = 10**9+7
        n = len(arr)
        nse = [n]*n
        st = []
        for i in range(n-1,-1,-1):
            while st and st[-1][0] >= arr[i]:
                st.pop()
            if st:
                nse[i] = st[-1][1]
            st.append((arr[i],i))
        pse = [-1]*n
        st = []
        for i in range(n):
            while st and st[-1][0] > arr[i]:
                st.pop()
            if st:
                pse[i] = st[-1][1]
            st.append((arr[i],i))
        subarrmin = 0
        for i in range(n):
            subarrmin += (nse[i] - i)*(i - pse[i])*arr[i]
        nge = [n]*n
        st = []
        for i in range(n-1,-1,-1):
            while st and st[-1][0] <= arr[i]:
                st.pop()
            if st:
                nge[i] = st[-1][1]
            st.append((arr[i],i))
        pge = [-1]*n
        st = []
        for i in range(n):
            while st and st[-1][0] < arr[i]:
                st.pop()
            if st:
                pge[i] = st[-1][1]
            st.append((arr[i],i))
        subarrmax = 0
        for i in range(n):
            subarrmax += (nge[i] - i)*(i - pge[i])*arr[i]
        return subarrmax - subarrmin