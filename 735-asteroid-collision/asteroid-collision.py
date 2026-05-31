class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        st = deque()

        for i in range(n):
            if not st:
                st.append(asteroids[i])
                continue
            current = asteroids[i]
            while st:
                last = st.pop()
                if (last > 0 and current < 0):
                    al = abs(last)
                    ac = abs(current)
                    if al == ac:
                        break
                    if al > ac:
                        st.append(last)
                        break
                    else:
                        if not st:
                            st.append(current)
                            break
                        continue
                else:
                    st.append(last)
                    st.append(current)
                    break
        ans = []
        while st:
            ans.append(st.popleft())

        return ans        
        