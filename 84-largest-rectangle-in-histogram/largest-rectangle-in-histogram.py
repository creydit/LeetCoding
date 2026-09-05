class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #using next smaller element thing and stack
        #TC - O(3N) and SC - O(2N)
        n = len(heights)
        left = [0]*n
        right = [0]*n

        st = []
        left[0] = -1
        st.append(0)
        for i in range(1,n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if not st:
                left[i] = -1
            else:
                left[i] = st[-1]
            st.append(i)

        right[n-1] = n
        st.clear()
        st.append(n-1)
        for i in range(n-2,-1,-1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if not st:
                right[i] = n
            else:
                right[i] = st[-1]
            st.append(i)

        ans = 0
        for i in range(n):
            area = heights[i] * ((i - left[i]) + (right[i] - i) - 1)
            ans = max(ans, area)
        return ans

        #brute can be finding the next smallest element for each number by using 2 loops going
        #one left side and one right side
        # TC - O(n^2) and SC - O(1)
