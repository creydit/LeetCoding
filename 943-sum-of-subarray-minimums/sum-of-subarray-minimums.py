class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #Optimal using next smaller and previous smaller elements
        #TC - O(N) and SC - O(N)
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
        ans = 0
        for i in range(n):
            ans += (nse[i] - i)*(i - pse[i])*arr[i]
            ans %= mod
        return ans

        #TC - O(n^2) and SC - O(1)
        '''
        n = len(arr)
        ans = 0
        mod = 10**9 + 7
        for i in range(n):
            mini = arr[i]
            for j in range(i,n):
                mini = min(mini, arr[j])
                ans += mini
                ans %= mod
        return ans
        '''