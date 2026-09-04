class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #TC - O(2n) and SC - O(1)
        n = len(s)
        ans = 0
        left = 0 
        right = 0
        for i in s:
            if i=='(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, left + right)
            if right > left:
                left = 0
                right = 0
        left = 0
        right = 0
        for i in range(n-1,-1,-1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, left+right)
            if right < left:
                left = 0
                right = 0
        return ans

        #TC -O(n) and SC - O(n)
        '''
        n = len(s)
        ans = 0
        st = [-1]
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans = max(ans, i - st[-1])
        return ans
        '''