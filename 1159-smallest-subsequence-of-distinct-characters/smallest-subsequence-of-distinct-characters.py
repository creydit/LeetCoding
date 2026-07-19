class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st = []
        vis = [0]*26
        dic = [0]*26

        for i in s:
            dic[ord(i) - ord('a')] += 1
        
        for i in s:

            dic[ord(i) - ord('a')] -= 1

            if vis[ord(i)-ord('a')]:
                continue

            while st and st[-1] > i and dic[ord(st[-1]) - ord('a')] > 0:
                vis[ord(st[-1]) - ord('a')] = 0
                st.pop()

            st.append(i)
            vis[ord(i)-ord('a')] = 1
        
        return ''.join(st)