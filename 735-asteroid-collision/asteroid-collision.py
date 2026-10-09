class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n = len(asteroids)
        st = []
        for i in range(n):
            curr = asteroids[i]
            if curr > 0:
                st.append(curr)
            else:
                while st and st[-1] > 0 and -curr > st[-1]:
                    st.pop()
                if st and st[-1]==-curr:
                    st.pop()
                elif not st or st[-1] < 0:
                    st.append(curr)             
        return st



        